from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from apps.users.models import User
from apps.users.forms import UserForm, UserCreateForm


class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class Login(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')


def user_update(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user.bio = form.cleaned_data['bio']
            user.image = form.cleaned_data['image']
            user.save()
        return redirect('index')
    else:
        form = UserForm()
    return render(request, 'users/user_update.html', locals())


def user_profile(request, id):
    user_obj = get_object_or_404(User, id=id)
    return render(request, 'users/user_courses.html', locals())


