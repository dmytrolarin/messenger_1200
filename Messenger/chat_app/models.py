from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class ChatGroup(models.Model):
    name = models.CharField(max_length = 200)
    users = models.ManyToManyField(UserModel)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chat", kwargs = {"group_id": self.pk})
    

class ChatMessage(models.Model):
    content = models.TextField()
    author = models.ForeignKey(UserModel, on_delete = models.SET_NULL, null = True)
    chat_group = models.ForeignKey(ChatGroup, on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now_add = True)