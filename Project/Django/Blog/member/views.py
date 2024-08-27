from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login as django_login
from django.urls import reverse  # 추가


# Create your views here.
def sign_up(request):

    # form은 POST 요청일 경우, POST 데이터를 사용하여 생성되고
    # 그렇지 않으면 빈 폼을 생성합니다.
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {"form": form}
    return render(request, "registration/signup.html", context)


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())

        next = request.GET.get("next")
        if next:
            return redirect(next)
        
        return redirect(
            reverse("blog_list")
        )  # url을 찾는 reverse함수와 urls.py에 적은 name을 활용해 동적으로 작성

    else:
        form = AuthenticationForm(request)

    context = {"form": form}

    return render(request, "registration/login.html", context)
