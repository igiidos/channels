from django.conf.urls import url
from django.urls import path
from . import consumers, consumers2

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    url(r'^ws/chat/(?P<room_name>[^/]+)/2/$', consumers2.ChatConsumer),
]