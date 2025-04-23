'''

'''
from django.urls import path
from .consumers import ChatConsumer

#
ws_urlpatterns = [
    #
    path("chat/", ChatConsumer.as_asgi()) 
]