from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView

from .forms import LoginUserForm, RegisterUserForm, UserPasswordResetForm, UserPasswordResetConfirmForm
from .models import User


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
        users = User.objects.all()
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

   


     
