from django import forms
from apps.categories.models import Category, CategoryImage


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class CategoryImageForm(forms.ModelForm):
    class Meta:
        model = CategoryImage
        fields = ['image', ]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }