from django.contrib import admin
from django.urls import path

from chapter_01.views import user_list, user_info

urlpatterns = [
    path("users/", user_list),
    path("users/<int:user_id>/", user_info),
]
