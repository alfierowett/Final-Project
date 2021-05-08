from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    ownerCategory = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ownerJournal')
    def __str__(self):
        return self.name

class journalEntry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    entry = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    titleEntry = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titleEntry