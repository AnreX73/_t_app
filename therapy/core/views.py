from django.contrib.auth.views import LoginView
from django.shortcuts import render

from .forms import LoginUserForm


def index(request):
    context = {
        "title": "Index",
    }
    return render(request, "core/index.html", context=context)


class LoginUser(LoginView):
    template_name = "registration/login.html"
    form_class = LoginUserForm
    extra_context = {"title": "Login"}
