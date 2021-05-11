from django.shortcuts import render, redirect
from .models import journalEntry, Category
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

#View renders Journal Page, displaying user specific elements and loading content from models
@login_required
def journal(request):
    category = request.GET.get('category')
    if category == None:
        entries = journalEntry.objects.all().filter(owner=request.user)
    else:
        entries = journalEntry.objects.filter(category__name=category).filter(owner=request.user)


    categories = Category.objects.all()

    context = {'categories': categories, 'entries': entries}
    return render(request, 'journal/journal.html', context)

#Filter entries by ascending order
@login_required
def AscEntries(request):
    category = request.GET.get('category')
    if category == None:
        entries =journalEntry.objects.order_by('date_posted').filter(owner=request.user)
    else:
        entries = journalEntry.objects.filter(category__name=category).order_by('date_posted').filter(owner=request.user)

    categories = Category.objects.all()
    context = {'categories':categories, 'entries':entries}
    
    return render(request, 'journal/journal.html', context)

#Filter entries by descending order
@login_required
def DescEntries(request):
    category = request.GET.get('category')
    if category == None:
        entries = journalEntry.objects.order_by('-date_posted').filter(owner=request.user)
    else:
        entries = journalEntry.objects.filter(category__name=category).order_by('-date_posted').filter(owner=request.user)

    categories = Category.objects.all()
    context = {'categories':categories, 'entries':entries}
    
    return render(request, 'journal/journal.html', context)

#View loads selected entry and displays viewEntry.html with all entry details
@login_required
def viewEntry(request, pk):
    entry = journalEntry.objects.get(id=pk)
    if entry.owner == request.user:
        return render(request, 'journal/viewEntry.html', {'entry': entry})
    else:
        raise PermissionDenied()

#function receives POST request to create a new journal entry
@login_required
def newEntry(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        entry = request.FILES.getlist('entry')

        print(request.POST)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        else:
            category = None


        entry = journalEntry.objects.create(
            category=category,
            titleEntry=data['titleEntry'],
            entry=data['entry'],
            owner=request.user,
        )

        return redirect('journal')

    context = {'categories':categories}
    return render(request, 'journal/newEntry.html', context)

#Private key passed for journal entry to be deleted from database
@login_required
def deleteEntry(request, pk):
    entry = journalEntry.objects.get(id=pk)

    entry.delete()
    return redirect('journal')
    return render(request, 'journal/journal.html')
