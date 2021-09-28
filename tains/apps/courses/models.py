from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.urls import reverse
from utils.slug_generator import unique_slug_generators
from apps.categories.models import Category
from apps.users.models import User


class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        related_name='course_category',
        on_delete=models.CASCADE,
        blank=True, null=True
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='course_user',
        null=True
    )

    def get_parent(self):
        return self.comment.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    def get_update(self):
        return reverse('course_update', kwargs={'slug': self.slug})

    def get_delete(self):
        return reverse('course_delete', kwargs={'slug': self.slug})


    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return f"{self.title}"


class CourseMedia(models.Model):
    image = models.ImageField(upload_to='image',
                              verbose_name='Картинки',
                              blank=True, null=True)
    video = models.FileField(upload_to='video',
                             verbose_name='Видео',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name='course_media'
    )

    def __str__(self):
        return f"{self.course.title}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_like')

    def __str__(self):
        return f"{self.user.username} -- {self.course.title}"


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Course)