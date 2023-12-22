from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
spotify_client = Spotify(auth_manager=auth_manager)


class SpotifyTopTracksView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        tracks = spotify_client.artist_top_tracks(artist_id=settings.SPOTIFY_ARTIST_ID)
        print("tracks")
        return Response(tracks)
