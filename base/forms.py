from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label=("Enter Password"), widget=forms.PasswordInput(attrs={'placeholder':'Enter 8 Digit Alphanumeric Password'}))
    password2 = forms.CharField(label=("Confirm Password"), widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username':None,
            'email':None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Enter Username...'}),
            'email': forms.EmailInput(attrs={'placeholder':'Enter Email...'}),
        }