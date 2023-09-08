from django.core import exceptions
from django.shortcuts import render, redirect

from exam_prep.web.forms import ProfileCreateForm
from exam_prep.web.models import Profile

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

    return render(request, 'core/home-with-profile.html')


def add_album(request):
    return render(request, 'album/add-album.html')


def details_album(request, pk):
    return render(request, 'album/album-details.html')


def edit_album(request, pk):
    return render(request, 'album/edit-album.html')


def delete_album(request, pk):
    return render(request, 'album/delete-album.html')


def details_profile(request):
    return render(request, 'profiles/profile-details.html')


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
