from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]