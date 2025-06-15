from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True,
                               label='Имя пользователя или email',
                               widget=forms.TextInput(
                                   attrs={'class': 'my_input', 'readonly onfocus': "this.removeAttribute('readonly');",
                                          'autocomplete': 'off'}))

    password = forms.CharField(required=True, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'my_input'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'readonly': True,
            'onfocus': "this.removeAttribute('readonly')",
            'autocomplete': 'off',
            'class': 'my_input'
        })
    )

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(attrs={'class': 'my_input'})
    )

    first_name = forms.CharField(
        required=True,
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'my_input'})
    )

    last_name = forms.CharField(
        required=True,
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'my_input'})
    )

    sex = forms.IntegerField(
        widget=forms.RadioSelect(choices=User.SEX, attrs={'class': 'radio-select'}),
        label='Пол'
    )

    phone = forms.CharField(
        required=True,
        label='Телефон',
        widget=forms.TextInput(attrs={'class': 'my_input'})
    )

    password1 = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'my_input'})
    )

    password2 = forms.CharField(
        required=True,
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'my_input'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'photo', 'password1', 'password2', 'sex')


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={'class': 'my_input'}))
