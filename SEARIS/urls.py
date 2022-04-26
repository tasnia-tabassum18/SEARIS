"""SEARIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from importlib import resources
from django.contrib import admin
from django.urls import path, include


#app_name = resources
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('resources/', include('resources.urls', namespace='resources')),
    path('UploadDatabase/',include('UploadDatabase.urls', namespace='database')),
    path('classroomrec/', include('classroom_requirement.urls', namespace='classresources')),
    path('revenue/', include('revenue.urls', namespace='revenue')),
    path('analysis_of_the_number_of_sections/', include('analysis_of_the_number_of_sections.urls', namespace='resources')),
    path('number_sections_offered', include('number_sections_offered.urls', namespace='resources')),
]
