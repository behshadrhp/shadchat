from django.urls import path

from chat import consumers


ASGI_urlpatterns = [
    path('websocket/<str:username>/', consumers.ChatConsumer.as_asgi(), name="websocket"),    
]
