from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Category, Document
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

#View renders the document wallet, displaying user specific elements and loading content from models
@login_required
def documentWallet(request):
    category = request.GET.get('category')
    if category == None:
        files = Document.objects.filter(owner=request.user)
    else:
        files = Document.objects.filter(category__name=category).filter(owner=request.user)

    
    categories = Category.objects.filter(ownerCategory=request.user)

    context = {'categories': categories, 'files': files}
    return render(request, 'documentWallet/documentWallet.html', context)

#Function to display file view page, renders single chosen file
@login_required
def viewDocument(request, pk):
    file = Document.objects.get(id=pk)
    if file.owner == request.user:
        return render(request, 'documentWallet/viewDocument.html', {'file': file})
    else:
        raise PermissionDenied()

#Filter stored files by ascending order
@login_required
def AscWallet(request):
    category = request.GET.get('category')
    if category == None:
        files = Document.objects.order_by('fileDate').filter(owner=request.user)
    else:
        files = Document.objects.filter(category__name=category).order_by('fileDate').filter(owner=request.user)

    categories = Category.objects.all()
    context = {'categories':categories, 'files':files}
    
    return render(request, 'documentWallet/documentWallet.html', context)

#Filter stored files by descending order
@login_required
def DescWallet(request):
    category = request.GET.get('category')
    if category == None:
        files = Document.objects.order_by('-fileDate').filter(owner=request.user)
    else:
        files = Document.objects.filter(category__name=category).order_by('-fileDate').filter(owner=request.user)

    categories = Category.objects.all()
    context = {'categories':categories, 'files':files}
    
    return render(request, 'documentWallet/documentWallet.html', context)

#function receives POST request to create a new file within wallet
@login_required
def newDocument(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        files = request.FILES.getlist('files')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['categoryNew'] != '':
            category, created = Category.objects.get_or_create(
                name=data['categoryNew'],
                ownerCategory=request.user)
        else:
            category = None

        for file in files:
            file = Document.objects.create(
            category=category,
            title=data['title'],
            file=file,
            owner=request.user,
        )

        return redirect('documentWallet')

    context = {'categories':categories}
    return render(request, 'documentWallet/newDocument.html', context)

#Private key passed for element to be deleted from database
@login_required
def deleteDocument(request, pk):
    file = Document.objects.get(id=pk)

    file.delete()
    return redirect('documentWallet')
    return render(request, 'documentWallet/viewDocument.html')

#httpResponse to handle error of pdf files source being from the same origin as page
@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")