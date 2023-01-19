import os
import youtube_dl
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class Playlist(object):
    def __init__(self,id , title):
        self.id = id
        self.title = title


class Song(object):
    def __init__(self):
        pass
        

class YouTubeClient:
    def __init__(self,credentials_location):
        youtube_dl.utils.std_headers['User-Agent'] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(credentials_location, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

        self.youtube = youtube

    def getPlaylist(self):
        request = self.youtube.playlists().list(part="id,snippet",maxResults=25,mine=True)
        respose = request.execute()

        playlists = [Playlist(item['id'], item['snippet']['title']) for item in respose["items"]]
        return playlists


    def getVideosFromPlaylist(self,playlist_Id):
        songs= []
        request = self.youtube.playlistItems().list(part="id,snippet",maxResults=25,playlistId=playlist_Id)
        response = request.execute()

        for item in response['items']:
            videoId = item['snippet']['resourceId']['videoId']
            artist, track = self.getArtistandTrackFromVideo(videoId)
            if artist and track:
                songs.append(Song())
        
        return songs

    def getArtistandTrackFromVideo(self,videoId):
        video = []
        youtubeurl = f"https://www.youtube.com/watch?v={videoId}"

        video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(youtubeurl, download=False)
        print(video['title'])
        artist = video[0]['title']
        return artist, track
    
