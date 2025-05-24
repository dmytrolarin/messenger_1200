'''
consumers.py - файл, який обробляє логіку веб-сокет запитів, аналог views.py
'''
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .forms import MessageForm
from channels.db import database_sync_to_async
from .models import ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    '''
    Створюємо клас ChatConsumer, який відповідає за з'єднання сервера з клієнтом. Він відловлює та обробляє ws запити 
    '''
    # Ім'я групи для користувачів
    # GROUP_NAME = "chat"
    async def connect(self):
        '''
        Метод connect відпрацьовує, коли користувач надсилає запит про підключення
        '''
        self.group_id = str(self.scope['url_route']['kwargs']['group_id'])
        await self.channel_layer.group_add(
            self.group_id, 
            self.channel_name
        )
        print(self.scope["user"])
        # Запит про підключення схвалений
        await self.accept()

    async def receive(self, text_data):
        '''
            Метод receive спрацьовує, коли сервер отримує повідомленя від клієнта
        '''
        await self.save_message(text_data)

        # Відправляємо повідомлення всім участникам групи
        await self.channel_layer.group_send(
            # Вказуємо назву групи
            self.group_id, 
            {
                # Вказуємо тип обробника (метод, що викличиться для відправки повідомлення)
                "type": "send_message_to_chat",
                # Передаємо повідомлення користувача через ivent, send_message_to_chat
                "text_data": text_data,
                "username": self.scope["user"].username,
            }
        )
        
    async def send_message_to_chat(self, event):
        '''
        Метод, який надсилає повідомлення усім участникам групи 
        '''

        # Перетворюємо текст з формату json у python словник
        dict_data = json.loads(event["text_data"])
        # Передаємо дані у форму для валідації
        form = MessageForm(dict_data)
        # У випадку якщо всі поля валідні
        if form.is_valid():
            # Надсилаємо повідомленя назад через WebSocket клієнту
            text_to_send = f"{event['username']}: {dict_data['message']}"
            text_data = json.dumps({"message": text_to_send}, ensure_ascii = False)
            await self.send(text_data = text_data)
        else:
            # Виводимо помилку, якщо форма не валідна
            print("Error, form isnt valid!")

    @database_sync_to_async
    def save_message(self, message_data):
        user = self.scope['user']
        message_data = json.loads(message_data)
        message = ChatMessage.objects.create(
            content = message_data['message'],
            author = user,
            chat_group_id = self.group_id
        )