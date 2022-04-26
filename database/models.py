from os import name

from django.db import models

# Create your models here.


class charField1(models.CharField):
    choicesofdays = (
    ('S', 'Sunday'),
    ('M', 'Monday'),
    ('T', 'Tuesday'),
    ('W', 'Wednesday'),
    ('ST','ST'),
    ('MW', 'MW')
    )
       
class charField2(models.CharField):
    sessionlist=(
    ('Autumn','Aut' ), ('Summer','Su'),('Spring','S')    
    )





class classroom_t(models.Model):
    room_id = models.CharField(db_column='room_id', primary_key=True, max_length=10)
    room_c = models.IntegerField(db_column='room_capacity', blank=True, null=True)

    class Meta:
        db_table = 'classroom_t'

class course_t(models.Model):
    course_ID = models.CharField(db_column='course_id', primary_key=True, max_length=10)
    course_name = models.CharField(db_column='course_name', max_length=50, blank=True, null=True)
    credit_hours = models.IntegerField(db_column='credit_hours', blank=True, null=True)

    class Meta:
       db_table = 'course_t'
class coofferedwith_t(models.Model):
    cooffered_c = models.CharField(db_column='cooffered_c', primary_key=True, max_length=10)
    course_id = models.ForeignKey('course_t', models.DO_NOTHING, db_column='course_id', blank=True, null=True)

    class Meta:
        db_table = 'coofferedwith_t'





class department_t(models.Model):
    dept_id = models.CharField(db_column='dept_id', primary_key=True, max_length=5)
    dept_name = models.CharField(db_column='dept_name', max_length=50, blank=True, null=True)
    school_title = models.ForeignKey('school_t', models.DO_NOTHING, db_column='school_title', blank=True, null=True)

    class Meta:
        db_table = 'department_t'


class faculty_t(models.Model):
    faculty_id = models.CharField(db_column='faculty_id', max_length=4, primary_key=True)
    faculty_name = models.CharField(db_column='faculty_name', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'faculty_t'

#blank = true means that attribute can be left blank in django forms
class school_t(models.Model):
    school_title = models.CharField(db_column='school_title', primary_key=True, max_length=5)
    school_name = models.CharField(db_column='school_name', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'school_t'


class section_t(models.Model):
    section_number= models.IntegerField(db_column='section_number', blank=True, null=True)
    section_no = models.IntegerField(db_column='section_no', primary_key= True)
    course_id = models.ForeignKey('course_t', models.DO_NOTHING, db_column='course_id', blank=True, null=False)
    dept_id = models.ForeignKey('department_t', models.DO_NOTHING, db_column='dept_id', blank=True, null=False)
    
    session_name = models.CharField(db_column='session_name', max_length=10, null=False)
    days = models.CharField(db_column='days', max_length=2)

    syear =  models.CharField(db_column='syear', max_length=4,null=False)
    faculty_id = models.ForeignKey('faculty_t', models.DO_NOTHING, db_column='faculty_id', blank=True, null=True)
    room_id = models.ForeignKey('classroom_t', models.DO_NOTHING, db_column='room_id', blank=True, null=True)
    capacity = models.IntegerField(db_column='capacity', blank=True, null=True)
    enroll_capacity = models.IntegerField(db_column='enroll_capacity', blank=True, null=True) 
    block_status = models.IntegerField(db_column='block_status', blank=True, null=True)

    start_time =  models.CharField(max_length=4,db_column='start_time', blank=True, null=True)
    end_time =  models.CharField(max_length=4, db_column='end_time', blank=True, null=True)

#unique_together is used to make two or more model fields to be unique so using it as we have more than 2 pkey.
    class Meta:
        db_table = 'section_t'
        unique_together = ('course_id', 'dept_id', 'session_name', 'syear', 'section_no')


        