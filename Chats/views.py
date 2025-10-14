from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ChatView(request):
    return render(request,'Chats/chat_room.html')
    
