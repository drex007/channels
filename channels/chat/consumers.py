import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatRoomConsumer(AsyncWebsocketConsumer):
    pass