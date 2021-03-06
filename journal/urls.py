from django.urls import path
from . import views

#Set URL paths within the Journal app

urlpatterns = [
    path('', views.journal, name='journal'),
    path('addEntry/', views.newEntry, name='newEntry'),
    path('viewEntry/<str:pk>/', views.viewEntry, name='viewEntry'),
    path('deleteEntry/<str:pk>/', views.deleteEntry, name='deleteEntry'),
    path('AscEntries/', views.AscEntries, name='AscEntries'),
    path('DescEntries/', views.DescEntries, name='DescEntries'),
]
