from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendarAlerts, name='calendar'),
    path('alerts/', views.Alerts, name='alerts'),
]
