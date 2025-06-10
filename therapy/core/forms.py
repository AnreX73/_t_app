from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True,
                       label='Имя пользователя или email',)

    password = forms.CharField(required=True,label='Пароль',
                               widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True,label='Имя пользователя ',)

    email = forms.EmailField(required=True,
                            label='Email' )

    first_name = forms.CharField(required=True,
                                 label='Имя')

    last_name = forms.CharField(required=True,
                                label='Фамилия')

    phone = forms.CharField(required=True,
                            label='Телефон')
    
    password1 = forms.CharField(required=True,
                                label='Пароль',
                                widget=forms.PasswordInput)

    password2 = forms.CharField(required=True,
                                label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','phone','photo', 'password1', 'password2')
