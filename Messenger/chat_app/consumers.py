'''
consumers.py - файл, який обробляє логіку веб-сокет запитів, аналог views.py
'''
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .forms import MessageForm

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
        # Запит про підключення схвалений
        await self.accept()

    async def receive(self, text_data):
        '''
            Метод receive спрацьовує, коли сервер отримує повідомленя від клієнта
        '''
        # Відправляємо повідомлення всім участникам групи
        await self.channel_layer.group_send(
            # Вказуємо назву групи
            self.group_id, 
            {
                # Вказуємо тип обробника (метод, що викличиться для відправки повідомлення)
                "type": "send_message_to_chat",
                # Передаємо повідомлення користувача через ivent, send_message_to_chat
                "text_data": text_data,
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
            await self.send(text_data = event["text_data"])
        else:
            # Виводимо помилку, якщо форма не валідна
            print("Error, form isnt valid!")
