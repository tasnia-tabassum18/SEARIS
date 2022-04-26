from django.contrib import admin


# Register your models here.
from database import models

class Classroom_Admin(admin.ModelAdmin):  
    model = models.classroom_t
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.classroom_t,  Classroom_Admin)


class Faculty_Admin(admin.ModelAdmin):
    model = models.faculty_t

    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.faculty_t, Faculty_Admin)


class School_Admin(admin.ModelAdmin):
    model = models.school_t
    
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.school_t, School_Admin)


class Department_Admin(admin.ModelAdmin):
    model = models.department_t
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.department_t, Department_Admin)


class Course_Admin(admin.ModelAdmin):
    model = models.course_t
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.course_t, Course_Admin)


class CofferedWith_Admin(admin.ModelAdmin):
    model = models.coofferedwith_t
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]
    
admin.site.register(models.coofferedwith_t, CofferedWith_Admin)


class Section_Admin(admin.ModelAdmin):
    model = models.section_t
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.section_t, Section_Admin)