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