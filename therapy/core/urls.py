from django.urls import path, include

from .views import index, LoginUser, RegisterUser, profile
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('', index, name='home'),


]


urlpatterns += [
    path("users/", include("django.contrib.auth.urls")),
    path("login/", LoginUser.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),

]
