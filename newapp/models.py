from os import name

from django.db import models
from django import forms 

# Create your models here.

class course_t(models.Model):
    course_ID = models.CharField(db_column='course_id', primary_key=True, max_length=7)
    course_name = models.CharField(db_column='course_name', max_length=50, blank=True, null=True)
    credit_hours = models.IntegerField(db_column='credit_hours', blank=True, null=True)

    class Meta:
       db_table = 'course_t'

    objects = models.Manager()