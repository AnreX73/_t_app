from tkinter import W
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from datetime import timedelta


from .forms import LoginUserForm, RegisterUserForm, UserPasswordResetForm, UserPasswordResetConfirmForm
from .models import User, WorkerSchedule


def index(request):
    context = {
        "title": "Index",
    }
    return render(request, "core/index.html", context=context)


class LoginUser(LoginView):
    template_name = "registration/login.html"
    form_class = LoginUserForm
    extra_context = {"title": "Login"}


@login_required(login_url="/register/")
def profile(request):
    user = request.user
    if user.role == 1:
        users = User.objects.filter(role=2)
        context = {
            "user": user,
            "title": "Profile",
            "users": users
        }

        return render(request, "registration/admin_profile.html", context=context)
    elif user.role == 2:
        context = {
            "user": user,
            "title": "Profile",
        }

        return render(request, "registration/worker_profile.html", context=context)
    else:
        context = {
            "user": user,
            "title": "Profile",
        }

        return render(request, "registration/profile.html", context=context)


class RegisterUser(View):
    template_name = "registration/register.html"

    def get(self, request):
        context = {
            "form": RegisterUserForm(),
            "title": "регистрация",
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("profile")
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/user_password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/user_password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = UserPasswordResetConfirmForm 

   


@login_required
def user_profile(request, pk):
    profile_user = get_object_or_404(User, pk=pk)
    
    
    if request.user.role != User.Role.Admin and request.user != profile_user:
        raise PermissionDenied("Вы не имеете доступа к этому профилю")
    
    return render(request, 'registration/user_profile.html', {'profile_user': profile_user})

     
def worker_calendar(request, worker_id):
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
    return render(request, 'core/worker_calendar.html', context)