# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .services import get_motivational_response


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """When a user connects to the WebSocket, accept the connection."""
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # ✅ Add user to room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """When a user disconnects, remove them from the chat room group."""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """When a message is received, get AI response and broadcast to group."""
        data = json.loads(text_data)
        user_message = data['text']

        # ✅ Synchronous call wrapped with sync_to_async
        ai_response = await sync_to_async(get_motivational_response)(user_message)

        # ✅ Broadcast user message
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': user_message,
                'is_user': True
            }
        )

        # ✅ Broadcast AI response
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': ai_response,
                'is_user': False
            }
        )

    async def chat_message(self, event):
        """Send the message to the WebSocket client."""
        await self.send(text_data=json.dumps({
            'text': event['message'],
            'is_user': event.get('is_user', False)
        }))
