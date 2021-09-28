from django.shortcuts import render
from apps.comments.models import Comment
from apps.courses.models import Course


def comment_index(request, slug):
    course_obj = Course.objects.get(slug=slug)
    comments = course_obj.comment.all()
    return render(request, 'comments/index.html', locals())

