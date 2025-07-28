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


from .forms import LoginUserForm, RegisterUserForm, UserPasswordResetForm, UserPasswordResetConfirmForm, CrateBidForm
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

     

@login_required
def create_bid(request):
    form = CrateBidForm
    context = {
        "title": "Создание заявки",
        "form": form
    }
    return render(request, 'core/create_bid.html', context=context)