from django.shortcuts import render, redirect
from .models import TVShow

def index(request):
    context = {
        'allshows': TVShow.objects.all()
    }
    return render(request, "index.html", context)

def new(request):
    context = {
        'allshows': TVShow.objects.all()
    }
    return render(request, 'new.html', context)

def create(request):
    print(request.POST)
    TVShow.objects.create(title = request.POST['showTitle'],
                          network = request.POST['networkName'],
                          description = request.POST['showDesc'],
                          release = request.POST['relDate'])
    return redirect('/')

def show(request, show_id): 
    thisShow = TVShow.objects.get(id=show_id)
    print(thisShow)
    context = {
        'this_show':thisShow
    }
    
    print(TVShow.objects.get(id=show_id).title)
    return render(request, 'show.html', context)

def edit(request, show_id):
    thisShow = TVShow.objects.get(id=show_id)
    context = {
        'this_show':TVShow.objects.get(id=show_id)
    }
    # print(request.POST)
    return render(request, 'edit.html', context)

def update(request, show_id):
    thisShow = TVShow.objects.get(id=show_id)
    thisShow.title = request.POST['titleOfShow']
    thisShow.network = request.POST['networkName']
    thisShow.release = request.POST['relDate']
    thisShow.description = request.POST['showDesc']
    thisShow.save()
    return redirect('/') 

def destroy(request, show_id):
    TVShow.objects.get(id=show_id).delete()
    return redirect('/')