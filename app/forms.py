from django import forms
from .models import *

class Deptform(forms.Form):
    dept_no= forms.IntegerField()
    dname = forms.CharField()
    location = forms.CharField()

class Empform(forms.Form):
    DL=[[do.dept_no,do.dept_no] for do in Dept.objects.all()]
    dept_no=forms.ChoiceField(choices=DL)
    emp_no= forms.IntegerField()
    emp_name = forms.CharField(max_length=100)
