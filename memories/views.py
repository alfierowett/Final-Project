from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Category, Photo
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

#View renders Memories page, displaying user specific elements and loading content from models
@login_required
def memories(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(owner=request.user)
    else:
        photos = Photo.objects.filter(category__name=category).filter(owner=request.user)

    categories = Category.objects.filter(ownerCategory=request.user)
    context = {'categories':categories, 'photos':photos}
    
    return render(request, 'memories/memories.html', context)

#Filter photos by age of upload ascending
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

#Filter photos by age of upload descending
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

#Function to display selected photo with all related data
@login_required
def viewImage(request, pk):
    photo = Photo.objects.get(id=pk)
    if photo.owner == request.user:
        return render(request, 'memories/viewImage.html', {'photo': photo})
    else:
        raise PermissionDenied()
    

#function receives POST request to create a new photo/memory within users DB
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
                name=data['categoryNew'],
                ownerCategory=request.user)
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

#Private key passed for chosen photo to be deleted from database
@login_required
def deleteImage(request, pk):
    image = Photo.objects.get(id=pk)
    if image.owner == request.user:
        image.delete()
        return redirect('memories')
    else:
        raise PermissionDenied()
        


