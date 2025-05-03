from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import MessageForm


class ChatView(FormView):
    template_name = "chat_app/chat.html"
    form_class = MessageForm
