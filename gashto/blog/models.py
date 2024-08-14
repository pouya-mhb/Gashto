from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager (models.Manager):
    def get_published_posts(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

    '''
    The get_queryset() method of a manager returns the QuerySet that will be
    executed. You override this method to include your custom filter in the final
    QuerySet.
    '''


class Post (models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    CATEGORY_CHOICES = (
        ('Entertainment', 'Entertainment'),
        ('Sport', 'Sport'),
        ('Introduce', 'Introduce')
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='subtitle')
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=100, unique_for_date='publish_date')
    category = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, default='')
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    upadted_date = models.DateTimeField(auto_now=True)
    body = models.TextField()

    '''
    If you declare any managers for your model but you want
    to keep the objects manager as well, you have to add it explicitly to your model.
    '''
    objects = models.Manager()  # The default manager
    # The custom manager for getting all published posts
    publishedObjects = PublishedManager()

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month,
                                                 self.publish.day, self.slug])
