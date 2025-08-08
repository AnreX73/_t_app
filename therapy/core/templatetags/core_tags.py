from django import template
from django.shortcuts import get_object_or_404
from django.utils import timezone
import calendar

from core.models import *

cl = calendar.Calendar(firstweekday=0)


def month_calendar(year, month):
    return cl.itermonthdates(year, month)


today = timezone.now().date()
YEAR = today.year
MONTH = today.month

register = template.Library()


@register.inclusion_tag("core/include/worker_calendar.html")
def worker_calendar(worker_id=None, year=YEAR, month=MONTH):
    # Получаем работника
    worker = get_object_or_404(User, id=worker_id)
    # Получаем расписание работника

    working_week_days = WorkerSchedule.objects.filter(worker_id=worker_id).values_list(
        "day_of_week", flat=True
    )
    actual_calendar = month_calendar(year, month)
    worker_calendar = []
    for day in actual_calendar:
        if day < today or today.month != day.month:
            day_info = {
                "date": day,
                "style": "non-working-day",  # Стиль по умолчанию для нерабочих дней
            }
            worker_calendar.append(day_info)
        elif day.weekday() in working_week_days:

            day_info = {
                "date": day,
                "style": "working-day",  # Стиль по умолчанию для рабочих дней
            }
            worker_calendar.append(day_info)
        else:
            day_info = {
                "date": day,
                "style": "non-working-day",  # Стиль по умолчанию для нерабочих дней
            }
            worker_calendar.append(day_info)

    return {"worker": worker, "worker_calendar": worker_calendar}
