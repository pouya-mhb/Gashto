from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(
    #     upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='places')
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return self.title


class Item(models.Model):
    ITEM_TYPES = (
        ('food', 'Food'),
        ('drink', 'Drink'),
        ('other', 'Other'),
    )

    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)

    def __str__(self):
        return self.title


class Rate(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.rating}'


class Review(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'
