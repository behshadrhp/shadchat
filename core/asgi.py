import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from chat.routing import ASGI_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(ASGI_urlpatterns),
    }
)
