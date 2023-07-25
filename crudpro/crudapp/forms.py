from django import forms
from django.forms import ModelForm
from . models import Task

class TaskForm(ModelForm):
    task=forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control','width':'200px','placeholder':'enter your tasks'}))
    class Meta():
        model=Task
        fields='__all__'