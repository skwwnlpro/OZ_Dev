from django.contrib import admin
from chapter_02.models import ToDo


# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
