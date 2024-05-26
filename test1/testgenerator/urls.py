from django.urls import path
from .views import files

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path('', files, name='files'),
    
]