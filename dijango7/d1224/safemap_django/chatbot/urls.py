from django.urls import path
from . import views
app_name = "chatbot"
urlpatterns = [
    path("", views.chat, name="chat"),
    path("api/ask/", views.ask, name="ask"),
]
