from django.contrib import admin
from . models import Category, Document
# Register your models here for admin access

admin.site.register(Category)
admin.site.register(Document)