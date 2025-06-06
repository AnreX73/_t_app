from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.IntegerChoices):
        Admin = 1, 'Администратор'
        Worker = 2, 'Специалист'
        Customer = 3, 'Пользователь'

    email = models.EmailField(unique=True, verbose_name='email address')
    role = models.PositiveSmallIntegerField(choices=Role.choices, default=Role.Customer, verbose_name='кто по жизни')
    phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Телефон')
    photo = models.ImageField(upload_to='user.photos', blank=True, null=True, verbose_name='Фото')
    registration_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
