from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatRoom(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatRoom of {self.user.username}"

class Messages(models.Model):
    room=models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name='messages')
    sender=models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('user','User'),('bot','Bot')], default='user')
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in {self.room.user.username}'s room"
