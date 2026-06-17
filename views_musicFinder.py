from django.shortcuts import render
from .models import Music
# Create your views here.
def home(request):
    allmusic = Music.objects.all()
    song1 = request.POST.get("song","")
    artist1= request.POST.get("artist", "")
    year1 = request.POST.get("year", "")
    album1= request.POST.get ("album","")
    if song1:
        allmusic=allmusic.filter(
            song__icontains= song1 
        )
    if artist1:
        allmusic = allmusic.filter(
            artist__icontains = artist1
        )
    if year1:
        allmusic= allmusic.filter(
            year__icontains= year1
        )
    if album1:
        allmusic = allmusic.filter(
            album__icontains= album1
        )
    context = {
        "allmusic":allmusic
    }
    return render(request, 'musicfind.html', context)
