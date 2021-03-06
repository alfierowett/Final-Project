from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

#View renders calendar page, displaying user specific elements and loading content from models
@login_required
def calendar(request):
    events = calendarEvent.objects.filter(owner=request.user)
    context = {'events':events}
    
    return render(request, 'calendarAlerts/calendar.html', context)

@login_required
def AscCal(request):
    events = calendarEvent.objects.order_by('eventDeadline').filter(owner=request.user)
    context = {'events':events}
    
    return render(request, 'calendarAlerts/calendar.html', context)

@login_required
def DescCal(request):
    events = calendarEvent.objects.order_by('-eventDeadline').filter(owner=request.user)
    context = {'events':events}
    
    return render(request, 'calendarAlerts/calendar.html', context)

#function receives POST request to create a new event for the calendar
@login_required
def newEvent(request):
    if request.method == 'POST':
        data = request.POST
        event = request.FILES.get('event')

        event = calendarEvent.objects.create(
            descriptionEvent=data['descriptionEvent'],
            event=data['event'],
            eventDeadline=data['eventDeadline'], 
            owner=request.user, 
        )

        return redirect('calendar')

    context = {'categories':categories}
    return render(request, 'calendarAlerts/calendar.html', context)

#Private key passed for element to be deleted from database
@login_required
def deleteEvent(request, pk):
    event = calendarEvent.objects.get(id=pk)
    if event.owner == request.user:
        event.delete()
        return redirect('calendar')
    else:
        raise PermissionDenied()
        


