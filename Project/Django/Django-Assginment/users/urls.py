from django.contrib import admin
from django.urls import path, include

from users.views import sign_up, login

urlpatterns = [
    path("", include("django.contrib.auth.urls"), name="logout"),
    path("login/", login, name="login"),
    path("signup/", sign_up, name="signup"),
]
