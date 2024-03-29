import os

from spotify_client import SpotifyClient
from youtube_client import YouTubeClient


def run():
    youtube_client = YouTubeClient('./creds/client_secrets.json')
    spotify_client = SpotifyClient("BQB-mj_OQmU4zu1iejI9KszJqdFK7MTr7urp9BoBEmJ0KdzhtfER_xtu6KauJYRsxJ1KfZhEtzQ38XYR0FxqsdjtWPDxiyUPyDF06nhAxAFpUIUiTDLYT89EIeYqNNPwVA7D527Jcbyts5BjPJIIRgGHAHS8ry2A80AfHixyv-FeHM7rVy9ID0sgIOwoc4mF8h3QCzdw6_LI2CbZCBSQ4ph_patCWDnEwztd3YHiNnbtO5YUzS1ovJnwCjzfZETH")
    playlists = youtube_client.get_playlists()
    
    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")
    
    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)}")
    
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist} - {song.track} to your Spotify Liked Songs")
        

if __name__ == '__main__':
    run()
