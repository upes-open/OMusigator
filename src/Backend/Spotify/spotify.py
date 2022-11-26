import spotipy
from spotipy.oauth2 import SpotifyOAuth

# authentication to spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="16ad531f0d504fe096e9d97500577b6d",
                                               client_secret="0438e44fbb2141e5b91d7f420cb3aa3e",
                                               redirect_uri="http://example.com",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# get the tracks of the playlist

def show_tracks(tracks):

    for i, item in enumerate(tracks['items']):
        track = item['track']
        print ("%d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))

#get the playlists of the user

playlists = sp.user_playlists('spotify')

for playlist in playlists['items']:
    if playlist['owner']['id'] == 'spotify':
        print (playlist['name'])
        print ('total tracks', playlist['tracks']['total'])
        results = sp.user_playlist('spotify', playlist['id'],
            fields="tracks,next")
        tracks = results['tracks']
        show_tracks(tracks)
        while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks)

#get tracks by playlist URL

def playlist_songs_by_id():
    playlist = sp.user_playlist('spotify', '37i9dQZF1DXcBWIGoYBM5M')
    print(playlist['name'])
    print('  total tracks', playlist['tracks']['total'])
    for track in playlist['tracks']['items']:
        print('    ', track['track']['name'])

#list the playlists of currently logged in user 

def list_playlists():
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        print(playlist['name'])
