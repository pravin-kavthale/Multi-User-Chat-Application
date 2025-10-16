from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import ChatRoom, Messages
from .serializers import MessageSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ChatView(request):
    return render(request, 'Chats/chat_room.html')

class ChatHistoryAPIView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            room = ChatRoom.objects.get(user=user)
            messages = Messages.objects.filter(room=room).order_by('timestamp')
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except User.DoesNotExist:  
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except ChatRoom.DoesNotExist: 
            return Response({"error": "Chat room not found"}, status=status.HTTP_404_NOT_FOUND)
