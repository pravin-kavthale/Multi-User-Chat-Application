# Chats/consumers.py
import django
django.setup()

# Chats/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
import asyncio
from datetime import datetime
from .models import ChatRoom, Messages
from django.contrib.auth.models import User
from .bot import get_bot_response

import time
from datetime import timedelta
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        self.room_group_name = f"chat_{self.username}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Send previous messages
        room = await self.get_room(self.username)
        messages = await self.get_messages(room)
        for msg in messages:
            await self.send(text_data=json.dumps({
                'message': msg.content,
                'role': msg.role,
                'timestamp': str(msg.timestamp)
            }))

        # Welcome message
        await self.send(text_data=json.dumps({
            'message': f'Hello {self.username}, welcome to your chat room!',
            'role': 'bot',
            'timestamp': str(datetime.now())
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)# takes json stringand convert it into python object
        user_message = data['message']
        room = await self.get_room(self.username)

        #Rate limiting: Allow max 2 message in a minute
        allowed= await self.check_rate_limit(room)
        if not allowed:
            await self.send(text_data=json.dumps({
                'message': 'Rate limit exceeded!!!!!!        Please wait before sending more messages.',
                'role': 'bot',
                'timestamp': str(datetime.now())
            }))
            return

        # Save user message
        await self.save_message(room, user_message, 'user')

        await self.send(text_data=json.dumps({
            'message': user_message,
            'role': 'user',
            'timestamp': str(datetime.now())
        }))

        # Bot response
        await asyncio.sleep(2)
        bot_response = await get_bot_response(user_message)
        await self.save_message(room, bot_response, 'bot')

        await self.send(text_data=json.dumps({
            'message': bot_response,
            'role': 'bot',
            'timestamp': str(datetime.now())
        }))
    
    @sync_to_async
    def check_rate_limit(self,room):
        one_miute_ago= timezone.now() - timedelta(minutes=1)
        message_count= Messages.objects.filter(room=room, role='user', timestamp__gte=one_miute_ago).count()
        return message_count < 2

    # Helper methods

    @sync_to_async
    def get_room(self, username):
        user = User.objects.get(username=username)
        room, created = ChatRoom.objects.get_or_create(user=user)
        return room

    @sync_to_async
    def get_messages(self, room, limit=20):
        return list(Messages.objects.filter(room=room).order_by('-timestamp')[:limit])

    @sync_to_async
    def save_message(self, room, content, role):
        Messages.objects.create(
            room=room,
            sender=room.user,
            content=content,
            role=role
        )
