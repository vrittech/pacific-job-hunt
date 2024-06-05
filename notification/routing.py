from django.urls import path 
from . import consumers

websocket_urlpatterns = [
    path('ws/notification/', consumers.MyAsyncConsumer.as_asgi())
]