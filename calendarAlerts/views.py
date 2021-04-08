from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def calendar(request):
    tasks = toDo.objects.all()

    context = {'tasks': tasks}
    return render(request, 'calendarAlerts/calendar.html', context)


