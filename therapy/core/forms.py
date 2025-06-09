from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, help_text='или email',
                               widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Username'}))

    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form_control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True,
                               widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Username'}))

    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'Email'}))

    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'First name'}))

    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Last name'}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form_control', 'placeholder': 'Password'}))

    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form_control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
