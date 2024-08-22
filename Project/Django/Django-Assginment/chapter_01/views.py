from django.shortcuts import render
from .fake_db import user_db


# Create your views here.
def user_list(request):
    user = user_db
    context = {"user_list": user}
    return render(request, "user_list.html", context)


def user_info(request, user_id):
    user = user_db[user_id]
    context = {"user": user}
    return render(request, "user_info.html", context)
