from django.db import models
from django.contrib.auth.models import User

# Create your models here for all content used in app


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    ownerCategory = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    imageDate = models.DateTimeField(auto_now_add=True)
    descriptionImage = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descriptionImage