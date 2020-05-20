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
    context = {
        'this_show':TVShow.objects.get(id=show_id)
    }
    print(TVShow.objects.get(id=show_id).title)
    return render(request, 'show.html', context)

def edit(request, show_id):
    pass 

def update(request, show_id):
    pass 

def destroy(request, show_id):
    pass 