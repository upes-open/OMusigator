from youtube_client import YouTubeClient
from spotify_client import SpotifyClient
import os

def run():
    youtube_client = YouTubeClient('client_secrets.json')
    spotify_client = SpotifyClient("BQC8FJk4DRlY6GnqDjHxChvPt3buChtWxDJU4CJlkcbvNdLJa7zVkHcuu-KEpSD4DTJqKbcQT9FHQQ-hI_uDDTn1N5dBkBPNBew39V3sk7ifd3xbawPZgyVdlaOis-Lw4vPCZtVYaMeWx_X6emv81qR32xNlwn3---SFqH58YH18MYiEWKd1AoVBOpplcBa0qpIgoIWBfN8h-Q_w")
    playlists = youtube_client.getPlaylist()

    for index, playlist in enumerate(playlists):
        print( f"{index}: {playlist.title}")
    
    choice = int(input("Enter your choice: ")) 
    chosenPlaylist = playlists[choice]
    print(f"You chose: {chosenPlaylist.title}")

    songs = youtube_client.getVideosFromPlaylist(chosenPlaylist.id)
    print(f"Attempting to add {len(songs)}")

    for song in songs:
        spotifySongId = SpotifyClient.searchSong(song.artist, song.track)
        if spotifySongId:
            addedSong = SpotifyClient.addSongToSpotify(spotifySongId)
            if addedSong:
                print(f"Added {song.artist} - {song.track} to your Spotify Liked Songs")    

if __name__ == '__main__':
    run()
