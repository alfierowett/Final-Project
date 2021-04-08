from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Category, Photo

def memories(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories':categories, 'photos':photos}
    
    return render(request, 'memories/memories.html', context)

def viewImage(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'memories/viewImage.html', {'photo': photo})


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
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
            category=category,
            descriptionImage=data['descriptionImage'],
            image=image
        )

        return redirect('memories')

    context = {'categories':categories}
    return render(request, 'memories/newImage.html', context)

def deleteImage(request, pk):
    image = Photo.objects.get(id=pk)

    image.delete()
    return redirect('memories')


