from django.urls import path
from . import views

urlpatterns = [
    path('', views.memories, name='memories'),
    path('add/', views.newImage, name='new'),
    path('image/<str:pk>/', views.viewImage, name='photo'),
    path('deleteImage/<str:pk>/', views.deleteImage, name='deleteImage'),
]
