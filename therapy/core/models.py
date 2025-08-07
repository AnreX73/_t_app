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


class AdditionalMaterials(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(
        upload_to="additional_materials", blank=True, verbose_name="Изображение"
    )
    note = models.TextField(blank=True, verbose_name="Примечание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Дополнительные материалы"
        verbose_name_plural = "Дополнительные материалы"


class WorkerSchedule(models.Model):
    DAYS_OF_WEEK = [
        (0, "Пн"),
        (1, "Вт"),
        (2, "Ср"),
        (3, "Чт"),
        (4, "Пт"),
        (5, "Сб"),
        (6, "Вс"),
    ]

    worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": User.Role.Worker},
        verbose_name="Специалист",
        related_name="worker_schedule",
    )
    day_of_week = models.PositiveSmallIntegerField(
        choices=DAYS_OF_WEEK,
        verbose_name="День недели",
    )
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    appointment_duration = models.PositiveSmallIntegerField(
        verbose_name="Длительность приема",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(120),
        ],  # Продолжительность приема в минутах (от 1 до 120)
    )
    pre_entry_days = models.PositiveSmallIntegerField(
        default=15,
        verbose_name="количество дней для предварительной записи",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(90),
        ],  # Количество дней предзаписи (от 0 до 30)
    )

    def __str__(self):
        return f"{self.worker} - {self.get_day_of_week_display()}"

    class Meta:
        verbose_name = "Расписание специалиста"
        verbose_name_plural = "Расписания специалистов"


class Abonements(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    bids_count = models.PositiveSmallIntegerField(verbose_name="Количество посещений")
    price = models.PositiveIntegerField(verbose_name="Цена", default=0)
    note = models.TextField(blank=True, verbose_name="Примечание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"


class Bid(models.Model):
    class BidStatus(models.IntegerChoices):
        NEW = 1, "Новая"
        ACCEPTED = 2, "Подтверждена"
        DECLINED = 3, "Отклонена"
        DONE = 4, "Завершена"

    worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": User.Role.Worker},
        related_name="worker_%(class)s",
        verbose_name="Специалист",
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": User.Role.Customer},
        related_name="customer_%(class)s",
        verbose_name="Заказчик",
    )
    abonement = models.ForeignKey(
        Abonements, on_delete=models.CASCADE, default=1, verbose_name="Абонемент"
    )
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    status = models.PositiveSmallIntegerField(
        choices=BidStatus.choices,
        default=BidStatus.NEW,
        verbose_name="Статус заявки",
    )

    class ChildSex(models.IntegerChoices):
        MALE = 1, "Мужской"
        FEMALE = 2, "Женский"

    is_child_bid = models.BooleanField(default=False, verbose_name="Детская заявка")
    sex = models.PositiveSmallIntegerField(
        choices=ChildSex.choices,
        default=ChildSex.MALE,
        verbose_name="Пол ребенка",
    )

    child_name = models.CharField(
        max_length=100, verbose_name="Имя ребенка",default="."
    )
    child_age = models.PositiveSmallIntegerField(
        default=1, verbose_name="Возраст ребенка"
    )

    customer_note = models.TextField(blank=True, verbose_name="Заказчик примечание")
    admin_note = models.TextField(blank=True, verbose_name="Администратор примечание")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
