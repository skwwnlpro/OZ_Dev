from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings


# Create your views here.
def sign_up(request):

    # form은 POST 요청일 경우, POST 데이터를 사용하여 생성되고
    # 그렇지 않으면 빈 폼을 생성합니다.
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {"form": form}
    return render(request, "signup.html", context)
