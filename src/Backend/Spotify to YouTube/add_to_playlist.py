from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import os
import pickle

from search_in_yt import *

def make_service():
    credentials = None

    # if(os.path.exists("token.pickle")):
    #     print("Loading credentials from file...")
    #     with open("token.pickle","rb") as token:
    #         credentials = pickle.load(token)

    # if not credentials or not credentials.valid:
    #     if credentials and credentials.expired and credentials.refresh_token:
    #         print("Refreshing access token...")
    #         credentials.refresh(Request())
    #     else:
    #         print("fetching new tokens...")

    flow = InstalledAppFlow.from_client_secrets_file("src/Backend/Spotify to YouTube/client_secrets.json",scopes=["https://www.googleapis.com/auth/youtube"] )

    flow.run_local_server(port=8080, prompt='consent', authorization_prompt_message='')

    credentials = flow.credentials

        # with open("token.pickle","wb") as f:
        #         print("Saving credentials for later use...")
        #         pickle.dump(credentials,f)

    service = build(serviceName='youtube', version='v3', credentials=credentials)

    return service

def make_playlist(service, name):
    request = service.playlists().insert(part="snippet", body={"snippet": {"title": str(name)}})
    response = request.execute()

    return response['id']


def add_to_playlist(service, playlistId,items):
    res = []
    for i in items:
        request = service.playlistItems().insert(part='snippet', body={'snippet': {'playlistId': str(playlistId), 'resourceId': {'kind': 'youtube#video', 'videoId': i}}})
        response = request.execute()
        print("added")
        res.append(response)

    return res
