from django.urls import path
from . import views

app_name = 'classroom_requirement'
urlpatterns = [
    path('classroomrec/', views.classroom_req, name='classroom_requirement'),
]