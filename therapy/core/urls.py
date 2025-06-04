from django.urls import path, include

from .views import index, Register

urlpatterns = [
    path('', index, name='home'),


]


urlpatterns += [
    path("users/", include("django.contrib.auth.urls")),
    path("register/", Register.as_view(), name="register"),
]
