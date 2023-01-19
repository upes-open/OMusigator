import urllib.parse
import requests


class SpotifyClient(object):
    def __init__(self, apitoken):
    
        self.apitoken = apitoken

    def searchSong(self, artist, track):
        query = urllib.parse.quote(f"{artist} {track}")
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(url,headers= {"Content-Type": "application/json", "Authorization": f"Bearer {self.apitoken}"})
        responseJson = response.json()
        results = responseJson["tracks"]["items"]
        if(results):
            return results[0]['id']
        else:
            raise Exception("No songs found on spotify")

    def addSongToSpotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(url, json= {
            "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.apitoken}"
            }
        )
        return response.ok  