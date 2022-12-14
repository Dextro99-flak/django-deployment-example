from django import forms
from main_app.models import UserProfile
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput, max_length=120)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio',)