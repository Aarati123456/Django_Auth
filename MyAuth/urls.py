from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('custom_register/', views.custom_register, name='custom_register'),
    path ('custom_login/', views.custom_login, name='custom_login')
    
]