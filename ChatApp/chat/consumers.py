import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )
    async def receive(self,text_data):
        json_text_data = json.loads(text_data)
        message = json_text_data['message']
        username = json_text_data['username']
        await self.channel_layer.group_send(
            self.roomGroupName,
            {
                'type':'send.message',
                'message':message,
                'username':username
            }
        )
    async def send_message(self,event):
        message = event["message"]
        username = event["username"]
        await self.send(
            text_data=json.dumps({
                "message":message,
                "username":username
            })
        )

