from django.db import models
from django.urls import reverse


# Create your models here.
class ChatGroup(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chat", kwargs = {"group_id": self.pk})