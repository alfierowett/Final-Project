from django.db import models
from django.contrib.auth.models import User

# Create your models here for all content used in app

class calendarEvent(models.Model):
    event = models.TextField(null=False, blank=False)
    eventCreation = models.DateTimeField(auto_now_add=True)
    eventDeadline = models.TextField(null=False, blank=False)
    descriptionEvent = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descriptionEvent