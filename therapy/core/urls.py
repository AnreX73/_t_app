from django.urls import path


from .views import (
    index,
    LoginUser,
    RegisterUser,
    profile,
    UserPasswordResetView,
    UserPasswordResetConfirmView,
    create_worker_schedule,
    
    
)
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)


urlpatterns = [
    path("", index, name="home"),
    path("create_worker_schedule/", create_worker_schedule, name="create_worker_schedule"),

    
]


urlpatterns += [
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile, name="profile"),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="registration/user_password_reset_done" ".html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="registration/user_password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    
]
