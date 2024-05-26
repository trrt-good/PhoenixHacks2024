from django.urls import path
from .views import callPage

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path('', callPage, name='callPage'),
    
]