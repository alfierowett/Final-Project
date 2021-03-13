from django.shortcuts import render
from django.http import HttpResponse



def calendarAlerts(request):
    return render(request, 'calendarAlerts/calendar.html')


def Alerts(request):
    return render(request, 'calendarAlerts/alerts.html')