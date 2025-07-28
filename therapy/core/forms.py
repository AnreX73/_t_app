from re import A
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from .models import AdultBid

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Имя пользователя или email",
        widget=forms.TextInput(
            attrs={
                "class": "my_input",
                "readonly onfocus": "this.removeAttribute('readonly');",
                "autocomplete": "off",
            }
        ),
    )

    password = forms.CharField(
        required=True, label="Пароль", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "password")


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(
        max_length=150,
        required=True,
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "readonly": True,
                "onfocus": "this.removeAttribute('readonly')",
                "autocomplete": "off",
            }
        ),
    )

    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput)

    first_name = forms.CharField(required=True, label="Имя", widget=forms.TextInput)

    last_name = forms.CharField(required=False, label="Фамилия", widget=forms.TextInput)

    sex = forms.IntegerField(
        widget=forms.RadioSelect(choices=User.SEX, attrs={"class": "radio-select"}),
        label="Пол",
    )

    phone = forms.CharField(required=False, label="Телефон", widget=forms.TextInput)

    password1 = forms.CharField(
        required=True, label="Пароль", widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        required=True, label="Повторите пароль", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "sex",
            "photo",
            "password1",
            "password2",
        )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput)


class UserPasswordResetConfirmForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

    new_password1 = forms.CharField(
        required=True, label="Новый пароль", widget=forms.PasswordInput
    )

    new_password2 = forms.CharField(
        required=True, label="Повторите пароль", widget=forms.PasswordInput
    )


class CrateBidForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=User.objects.filter(role=User.Role.Worker), label="Специалист", widget=forms.Select(attrs={"class": "custom-select"}))
    class Meta:
        model = AdultBid
        fields = ("worker", "date", "time", "customer_note")