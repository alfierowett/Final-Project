from django.contrib import admin
from . models import *
# Register your models here for admin access

admin.site.register(journalEntry)
admin.site.register(Category)