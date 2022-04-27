#from django.views import views
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Import_csv)
]
