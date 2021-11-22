from django.urls import path
from django.contrib.auth.views import LogoutView
from apps.users.views import (
    UserCreate, Login,
    user_profile, user_update,
    favorite_add, fav_list)

urlpatterns = [
    path('profile/<int:id>/', user_profile, name='user_profile'),
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('user_update/<int:id>/', user_update, name='user_update'),
    path('fav/<str:slug>/', favorite_add, name='fav_add'),
    path('fav_list/', fav_list, name='fav_list')
]
