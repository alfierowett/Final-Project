from django.contrib import admin
from .models import Category, Photo

# Register your models here for admin access

admin.site.register(Category)
admin.site.register(Photo)