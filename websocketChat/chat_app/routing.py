from django.urls import path
from . import consumers

websocket_urlpatterns = [
  # path('ws/jwc/<str:groupkaname>/', consumers.MyJsonWebsocketConsumer.as_asgi()),
  path('ws/ajwc/<str:groupkaname>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]