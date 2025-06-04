from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import UserCreateForm
import re


def index(request):
    context = {
        "title": "Index",
    }
    return render(request, "core/index.html", context=context)


class Register(View):
    template_name = "registration/register.html"

    def get(self, request):
        context = {
            "form": UserCreateForm(),
            "title": "регистрация",
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username1 = form.cleaned_data["email"]
            username = re.sub("[^A-Za-z0-9]", "", username1)
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)
