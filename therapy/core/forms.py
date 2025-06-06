from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True,
                               widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Username'}))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form_control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

