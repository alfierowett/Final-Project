from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Category, Document
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.decorators import login_required

@login_required
def documentWallet(request):
    category = request.GET.get('category')
    if category == None:
        files = Document.objects.filter(owner=request.user)
    else:
        files = Document.objects.filter(category__name=category).filter(owner=request.user)

    
    categories = Category.objects.all()

    context = {'categories': categories, 'files': files}
    return render(request, 'documentWallet/documentWallet.html', context)

@login_required
def viewDocument(request, pk):
    file = Document.objects.get(id=pk)
    return render(request, 'documentWallet/viewDocument.html', {'file': file})

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
                name=data['categoryNew'])
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

@login_required
def deleteDocument(request, pk):
    file = Document.objects.get(id=pk)

    file.delete()
    return redirect('documentWallet')
    return render(request, 'documentWallet/viewDocument.html')

@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")