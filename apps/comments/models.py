from django.db import models
from apps.courses.models import Course
from apps.users.models import User


class Comment(models.Model):
    text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    created_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"
