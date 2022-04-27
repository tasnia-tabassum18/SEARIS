from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [

 
   path ('Login', views.Login, name='Login'),
]