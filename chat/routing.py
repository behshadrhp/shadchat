from django.urls import path

from chat import consumers


ASGI_urlpatterns = [
    path('websocket/', consumers.ChatConsumer.as_asgi(), name="websocket"),    
]
