from django.urls import path
from .views import chat_view, clear_chat, conversation_list, view_conversation, delete_conversation

urlpatterns = [
    path('', chat_view, name='chat'),
    path('clear/', clear_chat, name='clear_chat'),
    path('conversations/', conversation_list, name='conversation_list'),
    path('conversations/<int:conversation_id>/', view_conversation, name='view_conversation'),
    path('conversations/<int:conversation_id>/delete/', delete_conversation, name='delete_conversation'),
]
