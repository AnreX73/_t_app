from django.urls import path, include

from .views import index, LoginUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),


]


urlpatterns += [
    path("users/", include("django.contrib.auth.urls")),
    path("login/", LoginUser.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
