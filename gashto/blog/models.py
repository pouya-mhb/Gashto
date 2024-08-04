from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class PublishedManager (models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post (models.Model):
    STATUS_CHOICES = (
        # todo ('editing','Editing')
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='subtitle')
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=100, unique_for_date='publish_date')
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    upadted_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # The Custom manager

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title
