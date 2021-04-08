from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class journalEntry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    entry = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    titleEntry = models.TextField()

    def __str__(self):
        return self.titleEntry