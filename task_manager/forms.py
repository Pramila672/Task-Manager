from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Task 

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput())

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','desc','deadline']
        #fields = "__all__"

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','desc','deadline','status']
        #fields = "__all__"