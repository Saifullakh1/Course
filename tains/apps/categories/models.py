from django.db import models
from django.db.models.signals import pre_save
from utils.slug_generator import unique_slug_generators


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категории')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"{self.title} -- {self.slug}"


class CategoryImage(models.Model):
    image = models.ImageField(upload_to='category', verbose_name='Картинки')
    category = models.OneToOneField(
        Category,
        related_name='category_image',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.category.title}"


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Category)
