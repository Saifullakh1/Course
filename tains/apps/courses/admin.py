from django.contrib import admin
from apps.courses.models import Course, CourseMedia
from django.contrib.admin import ModelAdmin


class CourseMediaAdmin(admin.TabularInline):
    model = CourseMedia
    extra = 1


class CourseAdmin(ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    inlines = [CourseMediaAdmin]


admin.site.register(Course, CourseAdmin)

