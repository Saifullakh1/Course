from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apps.categories.models import Category, CategoryImage


class CategoryImageAdmin(admin.TabularInline):
    model = CategoryImage
    extra = 1


class CategoryAdmin(ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    inlines = [CategoryImageAdmin]


admin.site.register(Category, CategoryAdmin)

