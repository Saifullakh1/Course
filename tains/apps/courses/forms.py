from django import forms
from apps.courses.models import Course, CourseMedia


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['slug', 'pub_date', 'owner', 'favorites']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CourseMediaForm(forms.ModelForm):
    class Meta:
        model = CourseMedia
        fields = ['image', 'video', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
