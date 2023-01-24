import os
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
from auth.credentials import *

spotify_client_id = SP_CLIENT_ID
spotify_client_secret = SP_CLIENT_SECRET
youtube_api_key = os.environ.get("YT_API_KEY")

def connect(id, secret):
    sp =  spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=id, client_secret= secret))
    return sp

def fetch_playlist_using_id(api, id):
    playlist  = api.playlist(playlist_id = id)
    name = playlist['name']
    playlist_item = playlist['tracks']['items']

    return playlist_item, name

playlist_id = '3NXuDjnoyINmBPQDwC1Zl6'

api = connect(spotify_client_id, spotify_client_secret)
playlist_items = fetch_playlist_using_id(api, playlist_id)

print(json.dumps(playlist_items))