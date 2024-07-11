import json

from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from chat.models import Message, UserChannel

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

        self.person_username = self.scope["url_route"]["kwargs"]["username"]

        try:
            user_channel = UserChannel.objects.get(user=self.scope["user"])
            user_channel.channel = self.channel_name
            user_channel.save()
        except:
            user_channel = UserChannel.objects.create(
                user=self.scope["user"],
                channel=self.channel_name
            )

    def receive(self, text_data):
        received_data = json.loads(text_data)

        other_user = User.objects.get(username=self.person_username)

        message = Message.objects.create(
            user=self.scope["user"],
            send_message_to=other_user,
            message=received_data.get("message")
        )

        try:
            user_channel = UserChannel.objects.get(user=other_user)
            channel_name = user_channel.channel

            data = {
                "type": "get_receiver",
                "type_of_date": "new_message",
                "data": received_data.get("message")
            }
            async_to_sync(self.channel_layer.send)(channel_name, data)
        except:
            pass

    def get_receiver(self, event):
        data = {
            "type": "new_message",
            "message": event["data"]
        }
        self.send(text_data=json.dumps(data))
