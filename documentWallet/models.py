from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Document(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(null=False, blank=False)
    fileDate = models.DateTimeField(auto_now_add=True)
    title = models.TextField()

    def __str__(self):
        return self.title