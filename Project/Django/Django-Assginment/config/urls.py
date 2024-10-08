"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# from chapter_01.views import user_info, user_list
# from chapter_02.views import todo_list, todo_info

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("chapter_01.urls")),
    path("cbv/", include("todo.urls")),
    path("", include("todo.urls")),
    path("accounts/", include("users.urls")),
]
