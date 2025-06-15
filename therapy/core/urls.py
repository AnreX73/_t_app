from django.urls import path, include

from .views import index, LoginUser, RegisterUser, profile, UserPasswordResetView
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path('', index, name='home'),


]


urlpatterns += [
    path("login/", LoginUser.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/user_password_reset_done'
                                                                             '.html'), name='password_reset_done'),
    # Добавьте остальные URL для сброса пароля, если нужно:
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
