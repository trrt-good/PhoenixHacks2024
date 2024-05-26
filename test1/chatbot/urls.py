from django.urls import path
from .views import upload_file, chat

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path('upload/', upload_file, name='upload_file'),
    path('chat/', chat, name='chat'),
]