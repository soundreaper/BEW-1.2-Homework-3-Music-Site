from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('musician/<int:musician_id>', views.artist, name="artist"),
  path('album/<int:album_id>', views.album, name="album"),
  path('song/<int:song_id>', views.song, name="song")
]