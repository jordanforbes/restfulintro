from django.shortcuts import render, redirect
from django.contrib import messages

from .models import TVShow, TVManager

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
    errors = TVShow.objects.basic_validator(request.POST)
    
    print('errors',errors)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        print('failed to update')
        return redirect('/shows/new')
    else:
        TVShow.objects.create(title = request.POST['titleOfShow'],
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
    
    
    errors = TVShow.objects.basic_validator(request.POST)
    
    print('errors',errors)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        print('failed to update')
        return redirect('/shows/'+show_id+'/edit')
    else:
        thisShow.title = request.POST['titleOfShow']
        thisShow.network = request.POST['networkName']
        thisShow.release = request.POST['relDate']
        thisShow.description = request.POST['showDesc']
        thisShow.save()
        messages.success(request, "show updated!")
        print('successfully updated!')
    return redirect('/') 

def destroy(request, show_id):
    TVShow.objects.get(id=show_id).delete()
    return redirect('/')