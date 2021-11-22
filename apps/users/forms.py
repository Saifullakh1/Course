from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'image']