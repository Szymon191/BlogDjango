from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('publish', 'Published'))

    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now())
    body = models.TextField(max_length=250)
