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
    GROUP_NAME = "chat"
    async def connect(self):
        '''
        Метод connect відпрацьовує, коли користувач надсилає запит про підключення
        '''
        await self.channel_layer.group_add(
            self.GROUP_NAME, 
            self.channel_name
        )
        print(self.channel_name)
        # Запит про підключення схвалений
        await self.accept()

    async def receive(self, text_data):
        '''

        '''
        # 
        await self.channel_layer.group_send(
            # 
            self.GROUP_NAME, 
            {
                # 
                "type": "send_message_to_chat",
                # 
                "text_data": text_data,
            }
        )
        
    async def send_message_to_chat(self, event):
        '''
        
        '''

        #
        dict_data = json.loads(event["text_data"])
        #
        form = MessageForm(dict_data)
        #
        if form.is_valid():
            #
            await self.send(text_data = event["text_data"])
        else:
            #
            print("Error, form isnt valid!")
