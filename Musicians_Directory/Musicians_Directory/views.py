from django.shortcuts import render,redirect
from Album.models import Album
from Musician.models import Musician
def home(request):
    albums=Album.objects.all()
    # musicians=Musician.objects.all()
    return render(request,"home.html",{'albums':albums})
