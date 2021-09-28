from django.urls import path
from apps.categories.views import(
    CategoryDetailView,
    category_create, category_update, category_delete
)

urlpatterns = [
    path('detail/<str:slug>/', CategoryDetailView.as_view(), name='cat_detail'),
    path('create/', category_create, name='cat_create'),
    path('update/<str:slug>/', category_update, name='cat_update'),
    path('delete/<str:slug>/', category_delete, name='cat_delete'),
]