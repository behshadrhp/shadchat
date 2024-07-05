from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        
    def receive(self, text_data):
        print(text_data)
