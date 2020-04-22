from django.shortcuts import render
from .models import Musician, Album, Song

def home(request):
  context = {
    'musicians': Musician.objects.all()
  }
  return render(request, 'home.html', context)

def artist(request, musician_id):
  context = {
    'musician': Musician.objects.get(id=musician_id),
    'albums' : Album.objects.filter(artist=musician_id)
  }
  return render(request, 'artist.html', context)

def album(request, album_id):
  context = {
    'album': Album.objects.get(id=album_id),
    'songs': Song.objects.filter(album=album_id)
  }
  return render(request, 'album.html', context)

def song(request, song_id):
  context = {
    'song': Song.objects.get(id=song_id),
  }
  return render(request, 'song.html', context)