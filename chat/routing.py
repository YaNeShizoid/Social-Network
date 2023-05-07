from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:id>/', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/online/', consumers.OnlineStatusConsumer.as_asgi()),
]