"""
ASGI config for boschBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from websock.consumers import ModelConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boschBackend.settings')

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^training$", ModelConsumer.as_asgi()),
        ])
    ),
})
