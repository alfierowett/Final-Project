from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Category, Photo
from django.contrib.auth.decorators import login_required

@login_required
def memories(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(owner=request.user)
    else:
        photos = Photo.objects.filter(category__name=category).filter(owner=request.user)

    categories = Category.objects.all()
    context = {'categories':categories, 'photos':photos}
    
    return render(request, 'memories/memories.html', context)

@login_required
def AscMemories(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.order_by('imageDate').filter(owner=request.user)
    else:
        photos = Photo.objects.filter(category__name=category).order_by('imageDate').filter(owner=request.user)

    categories = Category.objects.all()
    context = {'categories':categories, 'photos':photos}
    
    return render(request, 'memories/memories.html', context)

@login_required
def DescMemories(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.order_by('-imageDate').filter(owner=request.user)
    else:
        photos = Photo.objects.filter(category__name=category).order_by('-imageDate').filter(owner=request.user)

    categories = Category.objects.all()
    context = {'categories':categories, 'photos':photos}
    
    return render(request, 'memories/memories.html', context)

@login_required
def viewImage(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'memories/viewImage.html', {'photo': photo})

@login_required
def newImage(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['categoryNew'] != '':
            category, created = Category.objects.get_or_create(
            name=data['categoryNew'])
            ownerCategory=request.user,
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
            category=category,
            descriptionImage=data['descriptionImage'],
            image=image,
            owner=request.user,
        )

        return redirect('memories')

    context = {'categories':categories}
    return render(request, 'memories/newImage.html', context)

@login_required
def deleteImage(request, pk):
    image = Photo.objects.get(id=pk)

    image.delete()
    return redirect('memories')


