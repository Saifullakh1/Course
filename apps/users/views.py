from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from apps.users.models import User
from apps.users.forms import UserForm, UserCreateForm
from apps.courses.models import Course


class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class Login(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')


def user_update(request, id):
    user = request.user
    form = UserForm(request.POST, request.FILES, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('user_profile', id=id)
    else:
        form = UserForm()
    return render(request, 'users/user_update.html', locals())


def user_profile(request, id):
    user_obj = get_object_or_404(User, id=id)
    return render(request, 'users/user_courses.html', locals())


def favorite_add(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if course.favorites.filter(id=request.user.id).exists():
        course.favorites.remove(request.user)
    else:
        course.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def fav_list(request):
    new = Course.objects.filter(favorites=request.user)
    return render(request, 'courses/like_courses.html', {'new': new})



