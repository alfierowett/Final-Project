from django.shortcuts import render
from django.http import HttpResponse



def journal(request):
    return render(request, 'journal/journal.html')

