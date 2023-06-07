from django.contrib import admin

from .models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("pk", "name_ru")
    list_display_links = ("pk", "name_ru")


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name_ru")
    list_display_links = ("pk", "name_ru")
