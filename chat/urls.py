from django.urls import path
from .views import chat_view, clear_chat

urlpatterns = [
    path('', chat_view, name='chat'),
    path('clear/', clear_chat, name='clear_chat'),  # New URL for clearing chat

]
