from django.urls import path
from . import views

#Set URL paths within the Memories feature
urlpatterns = [
    path('', views.memories, name='memories'),
    path('add/', views.newImage, name='new'),
    path('image/<str:pk>/', views.viewImage, name='photo'),
    path('deleteImage/<str:pk>/', views.deleteImage, name='deleteImage'),
    path('ascending/', views.AscMemories, name='AscMemories'),
    path('descending/', views.DescMemories, name='DescMemories'),
]
