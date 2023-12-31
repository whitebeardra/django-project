from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class shopping_item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField()
    objects = models.Manager()


    def __str__(self):
        return self.name

class images(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    objects = models.Manager()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name