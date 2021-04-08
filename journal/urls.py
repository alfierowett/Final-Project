from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('addEntry/', views.newEntry, name='newEntry'),
    path('viewEntry/<str:pk>/', views.viewEntry, name='viewEntry'),
    path('deleteEntry/<str:pk>/', views.deleteEntry, name='deleteEntry'),
]
