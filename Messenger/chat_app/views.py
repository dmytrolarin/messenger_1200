from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import MessageForm
from .models import ChatGroup

class ChatView(FormView):
    template_name = "chat_app/chat.html"
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        chat_group_id = self.kwargs["group_id"]
        data["chat_group"] = ChatGroup.objects.get(pk = chat_group_id)
        return data

    
class ChatGroupListView(ListView):
    model = ChatGroup
    template_name = "chat_app/groups.html"
    context_object_name = "list_groups"

    