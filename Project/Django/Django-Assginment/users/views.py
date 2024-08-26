from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def sign_up(request):

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {"form": form}
    return render(request, "registration/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "로그인 성공!")
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                messages.error(request, "로그인 실패, ID or PASSWORD 확인하세요")
        else:
            messages.error(request, "로그인 실패, ID or PASSWORD 확인하세요")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST or None)
#         if form.is_valid():
#             django_login(request, form.get_user())
#             return redirect(settings.LOGIN_REDIRECT_URL)
#     else:
#         form = AuthenticationForm()

#     context = {"form": form}
#     return render(request, "registration/login.html", context)
