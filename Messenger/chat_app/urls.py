from django.urls import path
from .views import ChatView, ChatGroupListView


urlpatterns = [
    path("chat/<int:group_id>", ChatView.as_view(), name="chat"),
    path("", ChatGroupListView.as_view(), name = "groups")
    
]