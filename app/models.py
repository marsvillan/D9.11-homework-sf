from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.SET_NULL, related_name='posts')
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL, related_name='posts')

    def __str__(self):
        return self.title
