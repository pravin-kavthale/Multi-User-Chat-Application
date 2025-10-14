from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.ChatView, name='chat_room'),  
]
