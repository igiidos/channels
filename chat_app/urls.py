from django.contrib import admin
from django.urls import path

from chat_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('one_index/', views.one_index, name='one_index'),
    path('<str:room_name>/', views.room, name='room'),
    path('<str:room_name>/2/', views.one_room, name='one_room')
]
