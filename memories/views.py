from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Category, Photo

def memories(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories, 'photos':photos}
    return render(request, 'memories/memories.html', context)

def viewImage(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'memories/viewImage.html', {'photo': photo})


def newImage(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['categoryNew'] != '':
            category, created = Category.objects.get_or_create(name=['categoryNew'])
        else:
            category = None


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


