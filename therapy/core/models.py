from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    SEX = (
        (1, "Мужской"),
        (2, "Женский"),
    )

    class Role(models.IntegerChoices):
        Admin = 1, "Администратор"
        Worker = 2, "Специалист"
        Customer = 3, "Пользователь"

    email = models.EmailField(unique=True, verbose_name="email address")
    sex = models.PositiveSmallIntegerField(choices=SEX, default=1, verbose_name="Пол")
    role = models.PositiveSmallIntegerField(
        choices=Role.choices, default=Role.Customer, verbose_name="кто по жизни"
    )
    phone = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="Телефон"
    )
    photo = models.ImageField(
        upload_to="user.photos", blank=True, null=True, verbose_name="Фото"
    )
    registration_date = models.DateField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]


class WorkerSchedule(models.Model):
    DAYS_OF_WEEK = [
        ("mon", "Понедельник"),
        ("tue", "Вторник"),
        ("wed", "Среда"),
        ("thu", "Четверг"),
        ("fri", "Пятница"),
        ("sat", "Суббота"),
        ("sun", "Воскресенье"),
    ]

    worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": User.Role.Worker},
        verbose_name="Специалист",
        related_name="worker_schedule",
    )
    day_of_week = models.CharField(
        max_length=3, choices=DAYS_OF_WEEK, verbose_name="День недели"
    )
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    appointment_duration = models.PositiveSmallIntegerField(
        verbose_name="Длительность приема",
        validators=[MinValueValidator(1), MaxValueValidator(120)],  # Продолжительность приема в минутах (от 1 до 120)
    )

    def __str__(self):
        return f"{self.worker} - {self.get_day_of_week_display()}"

    class Meta:
        verbose_name = "Расписание специалиста"
        verbose_name_plural = "Расписания специалистов"
