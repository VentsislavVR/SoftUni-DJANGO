from django.core import exceptions
from django.shortcuts import render, redirect

from exam_prep.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from exam_prep.web.models import Profile, Album

# Create your views here.

'''
· http://localhost:8000/ - home page 
· http://localhost:8000/album/add/ - add album page 
· http://localhost:8000/album/details/<id>/ - album details page 
· http://localhost:8000/album/edit/<id>/ - edit album page 
· http://localhost:8000/album/delete/<id>/ - delete album page 
· http://localhost:8000/profile/details/ - profile details page 
· http://localhost:8000/profile/delete/ - delete profile page
'''


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'albums':Album.objects.all(),
    }

    return render(request,
                  'core/home-with-profile.html',
                  context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request,
                  'album/add-album.html',
                  context)


def details_album(request, pk):
    album = Album.objects\
             .filter(pk=pk)\
             .get()
    context = {
        'album': album,
    }
    return render(request,
                  'album/album-details.html'
                  ,context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album':album,
    }
    return render(request,
                  'album/edit-album.html',
                  context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method=='GET':
        form = AlbumDeleteForm(instance=album)
    else:
        # Album.objects.filter(pk=pk).delete() not recommended!
        form = AlbumDeleteForm(request.POST,instance=album)
        if form.is_valid():
            form.save() # proer way to change the save in the form
            return redirect('index')

    context={
        'album':album,
        'form':form,
    }

    return render(request,
                  'album/delete-album.html'
                  ,context)


def details_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }

    return render(request,
                  'profiles/profile-details.html',
                  context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form,

    }
    return render(request,
                  'core/home-no-profile.html',
                  context)


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
