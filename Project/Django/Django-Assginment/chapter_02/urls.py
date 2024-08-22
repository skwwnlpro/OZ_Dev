from django.contrib import admin
from django.urls import path

from chapter_02.views import todo_list, todo_info

urlpatterns = [
    path("todo/", todo_list),
    path("todo/<int:todo_id>/", todo_info),
]
