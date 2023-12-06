from django.urls import path

from .views import SpotifyTopTracksView

app_name = "music"

urlpatterns = [
    path("spotify/top_tracks/", SpotifyTopTracksView.as_view(), name="spotify_top_tracks"),
]
