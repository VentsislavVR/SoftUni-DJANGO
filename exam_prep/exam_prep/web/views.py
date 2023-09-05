from django.shortcuts import render


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


def index(request):
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


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')
