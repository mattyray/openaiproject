import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """When a user connects to the WebSocket, accept the connection."""
        self.room_name = self.scope['url_route']['kwargs']['room_name']  # Dynamic room name
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """When a user disconnects, remove them from the chat room group."""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """When a message is received, broadcast it to everyone in the room."""
        data = json.loads(text_data)
        message = data['text']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'is_user': True
            }
        )

    async def chat_message(self, event):
        """Send the message to the WebSocket client."""
        await self.send(text_data=json.dumps({
            'text': event['message'],
            'is_user': event.get('is_user', False)
        }))
