from django.contrib.auth import get_user_model
from datetime import datetime
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
)
from django.utils.translation import gettext_lazy as _
from django import forms
import re

User = get_user_model()


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].label = _("Имя")
        self.fields["last_name"].label = _("Фамилия")
        self.fields["last_name"].required = False
        self.fields["password1"].help_text = None  # Убираем подсказки для пароля
        self.fields["password2"].help_text = None

    phone = forms.CharField(required=False)
    photo = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "password1",
            "password2",
            "photo",
        )
       
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        username = self.cleaned_data["email"]
        user.username = re.sub("[^A-Za-z0-9]", "", username)
        user.phone = self.cleaned_data["phone"]
        user.photo = self.cleaned_data["photo"]
        if commit:
            user.save()
        return user
