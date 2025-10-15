from django.urls import path
from . import views
from .views import ChatHistoryAPIView

urlpatterns = [
    path('chat/', views.ChatView, name='chat_room'),  
    path('api/history/<str:username>/', ChatHistoryAPIView.as_view(), name='chat-history'),
]
