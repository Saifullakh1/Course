from django.urls import path
from apps.courses.views import (
    CourseListView,
    CourseDetailView,
    CoursesGallery,
    SearchCourse,
    course_create, course_update,
    course_delete
)

urlpatterns = [
    path('', CourseListView.as_view(), name='index'),
    path('detail/<str:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('create/', course_create, name='course_create'),
    path('update/<str:slug>/', course_update, name='course_update'),
    path('delete/<str:slug>/', course_delete, name='course_delete'),
    path('courses/', CoursesGallery.as_view(), name='courses_gallery'),
    path('search/', SearchCourse.as_view(), name='search')
]
