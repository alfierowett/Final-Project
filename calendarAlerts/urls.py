from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('addEvent/', views.newEvent, name='newEvent'),
    path('deleteEvent/<str:pk>/', views.deleteEvent, name='deleteEvent'),
    path('ascending/', views.AscCal, name='AscCal'),
    path('descending/', views.DescCal, name='DescCal'),
]
