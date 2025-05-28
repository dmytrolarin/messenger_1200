from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import MessageForm
from .models import ChatGroup, ChatMessage
from django.shortcuts import redirect

class ChatView(FormView):
    template_name = "chat_app/chat.html"
    form_class = MessageForm

    def dispatch(self, request, *args, **kwargs):
        chat_group_id = self.kwargs['group_id']
        chat = ChatGroup.objects.get(pk = chat_group_id)
        user = request.user
        if user in chat.users.all():
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('groups')
       
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        chat_group_id = self.kwargs["group_id"]
        messages = ChatMessage.objects.filter(chat_group_id = chat_group_id)
        data["messages"] = messages
        data["chat_group"] = ChatGroup.objects.get(pk = chat_group_id)
        return data

    
class ChatGroupListView(ListView):
    model = ChatGroup
    template_name = "chat_app/groups.html"
    context_object_name = "list_groups"

    