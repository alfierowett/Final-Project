from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home/homepage.html')
    
@login_required
def links(request):
    return render(request, 'home/links.html')


