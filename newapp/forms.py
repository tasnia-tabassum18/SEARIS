from django import forms
 
from forms import FormHelper
from forms import Layout, Div, Submit, Row, Column, Field
 
from .models import course_t
 
class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = course_t
        fields =[ 'course_ID','course_name','credit_hours'
        ] 