import json
import re
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        raw_room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = re.sub(r'[^a-zA-Z0-9_-]', '_', raw_room_name)
        self.room_name = self.room_name[:99]
    
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        self.close(code)

    async def receive(self, text_data):
        # Print incoming data for debugging
        data_json = json.loads(text_data)

        event = {"type": "send_message", "message": data_json}

        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        data = event["message"]
        file_url = None

        # If there's a file attached in the message, process it
        if data.get("file"):
            file_url = data["file"]
        
        await self.create_message(data=data, file_url=file_url)

        response = {"sender": data["sender"], "message": data["message"], "file": file_url}

        await self.send(text_data=json.dumps({"message": response}))

    @database_sync_to_async
    def create_message(self, data, file_url):
        get_room = Room.objects.get(room_name=data["room_name"])

        if not Message.objects.filter(
            message=data["message"], sender=data["sender"]
        ).exists():
            new_message = Message.objects.create(
                room=get_room,
                message=data["message"],
                sender=data["sender"],
                file=file_url
            )
