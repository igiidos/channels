from django.contrib import admin
from django.urls import path

from chat_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room')
]
