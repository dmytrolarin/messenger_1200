from django.shortcuts import render
from django.views.generic.base import TemplateView


class ChatView(TemplateView):
    template_name = "chat_app/chat.html"