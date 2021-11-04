from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from apps.courses.forms import CourseForm, CourseMediaForm
from apps.courses.models import Course, CourseMedia, Like
from apps.categories.models import Category
from apps.comments.models import Comment


class CourseListView(generic.ListView):
    queryset = Course.objects.all()[:8]
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[:8]
        return context


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courses/course_detail.html'


def course_detail(request, slug):
    course = Course.objects.get(slug=slug)

    fav = bool

    if course.favorites.filter(id=request.user.id).exists():
        fav = True

    if 'comment' in request.POST:
        try:
            text = request.POST.get('text')
            comment_obj = Comment.objects.create(user=request.user, course=course, text=text)
            return redirect('course_detail', course.slug)
        except:
            print("Error")
    if 'like' in request.POST:
        try:
            like = Like.objects.get(user=request.user, course=course)
            like.delete()
        except:
            Like.objects.create(user=request.user, course=course)
    return render(request, 'courses/course_detail.html', locals())


class CoursesGallery(generic.ListView):
    model = Course
    paginate_by = 6
    template_name = 'courses/index_courses.html'
    context_object_name = 'courses'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()[:8]
        return context


class SearchCourse(generic.ListView):
    model = Course
    template_name = 'courses/course_search.html'
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = Course.objects.all()
        qury_obj = self.request.GET.get('course_title')
        if qury_obj:
            queryset = Course.objects.filter(
                Q(title__icontains=qury_obj) | Q(owner__username__icontains=qury_obj)
            )
        return queryset


@login_required
def course_create(request):
    form = CourseForm(request.POST or None)
    CourseMediaFormSet = inlineformset_factory(Course, CourseMedia, form=CourseMediaForm, extra=1)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            formset = CourseMediaFormSet(request.POST, request.FILES, instance=obj)
            if formset.is_valid():
                formset.save()
            return redirect('index')
    formset = CourseMediaFormSet()
    return render(request, 'courses/course_create.html', locals())


def course_update(request, slug):
    course = get_object_or_404(Course, slug=slug)
    form = CourseForm(request.POST, None, instance=course)
    CourseMediaFormSet = inlineformset_factory(Course, CourseMedia, form=CourseMediaForm, extra=1)
    if request.user == course.owner:
        if form.is_valid():
            obj = form.save()
            obj.owner = request.user
            obj.save()
            formset = CourseMediaFormSet(request.POST, request.FILES, instance=course)
            if formset.is_valid():
                formset.save()
                return redirect('index')
    formset = CourseMediaFormSet(instance=course)
    return render(request, 'courses/course_update.html', locals())


def course_delete(request, slug):
    if request.method == 'POST':
        course = Course.objects.get(slug=slug)
        if request.user == course.owner:
            course.delete()
        return redirect('index')
    return render(request, 'courses/course_delete.html')
