from django.contrib import admin
from .models import House

# Register your models here.


# HouseAdmin class는 ModelAdmin class로부터 모든 걸 inheritage 받아
# 이 ModelAdmin은 여러분의 model을 위한 admin 패널이고
# 이 Class가 admin을 하게 될 model은 House라고 합니다.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # Using The Pure Admin Inheritage Admin
    list_display = ["name", "price_per_night", "address", "pets_allowed"]
    list_filter = ["price_per_night", "pets_allowed"]
    search_fields = ["address_startswith"]
