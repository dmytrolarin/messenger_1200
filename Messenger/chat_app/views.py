from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .forms import MessageForm
from .models import ChatGroup, ChatMessage
from django.shortcuts import redirect


class ChatView(FormView):
    # Вказуємо шаблон для відображення
    template_name = "chat_app/chat.html"
    # Вказуємо форму з якою буде працювати клас
    form_class = MessageForm

    def dispatch(self, request, *args, **kwargs):
        '''
            Цей метод спрацьовує перед відображенням сторінки. У ньому прописується логіка, що повинна спрацьовувати перед відображенням сторінки.
        '''

        # Отримуємо параметр з динамічної URL-адреси
        chat_group_id = self.kwargs['group_id']
        # Шукаємо чат по його pk
        chat = ChatGroup.objects.get(pk = chat_group_id)
        # Отримуємо авторизованого користувача
        user = request.user
        # Якщо користувач є у чаті
        if user in chat.users.all():
            # Повертаємо звичайний виклик методу
            return super().dispatch(request, *args, **kwargs)
        else:
            # Якщо користувача немає - повертаємо на сторінку груп
            return redirect('groups')
       
    def get_context_data(self, **kwargs):
        '''
            Цей метод потрібен для обробки контексту, що буде переданий до шаблонізатору.
        '''
        # Отримуємо контекст
        data = super().get_context_data(**kwargs)
        # Отримуємо параметр з динамічної URL-адреси
        chat_group_id = self.kwargs["group_id"]
        # Отримуємо усі повідомлення цього чату
        messages = ChatMessage.objects.filter(chat_group_id = chat_group_id)
        # Додаємо повідомлення до контексту
        data["messages"] = messages
        # Передаємо чат у контекст
        data["chat_group"] = ChatGroup.objects.get(pk = chat_group_id)
        # Повертаємо змінений контекст
        return data

    
class ChatGroupListView(ListView):
    '''
        Створюємо класс для відображння спику груп.
    '''

    # Вказуємо модель, з якої будуть братися об'єкти
    model = ChatGroup
    # Вказуємо шаблон для відображення
    template_name = "chat_app/groups.html"
    # Вказуємо ім'я, за яким буде називатися наш список у шаблонізаторі
    context_object_name = "list_groups"

class PersonalChatListView(ListView):
    template_name = "chat_app/personal_chats.html" 
    context_object_name = "list_chats"

    def get_queryset(self):
        queryset = get_user_model().objects.exclude(pk=self.request.user.pk)
        return queryset

