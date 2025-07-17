from django import template
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

from core.models import *

register = template.Library()


@register.inclusion_tag('core/include/worker_calendar.html')
def worker_calendar(worker_id=None):
    # Получаем работника
    worker = get_object_or_404(User, id=worker_id)
    # Получаем расписание работника
    schedules =WorkerSchedule.objects.filter(worker_id=worker_id)
    # Текущая дата
    today = timezone.now().date()
    
    # Определяем начало и конец текущего месяца
    start_date = today.replace(day=1)  # Первый день текущего месяца
    next_month = start_date.replace(day=28) + timedelta(days=4)  # Переход на следующий месяц
    end_date = next_month - timedelta(days=next_month.day)  # Последний день текущего месяца

    # Создаем календарь
    calendar = []
    current_date = start_date
    while current_date <= end_date:
        day_info = {
            "date": current_date,
            "day_of_week": current_date.strftime("%a").lower(),  # День недели в формате 'mon', 'tue', и т.д.
            "is_past": current_date < today,  # Прошедшая дата
            "is_working": False,  # По умолчанию день не рабочий
            "style": "non-working-day"  # Стиль по умолчанию для нерабочих дней
        }

        # Проверяем, является ли день рабочим
        for schedule in schedules:
            if day_info["day_of_week"] == schedule.day_of_week:
                day_info["is_working"] = True
                day_info["style"] = "working-day"
                break

        # Если день прошедший, меняем стиль
        if day_info["is_past"]:
            day_info["style"] = "past-day"

        calendar.append(day_info)
        current_date += timedelta(days=1)

    # Передаем данные в шаблон
    context = {
        "worker": worker,
        "calendar": calendar,
        "today": today,
    }
    return context