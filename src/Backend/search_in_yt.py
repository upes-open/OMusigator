from googleapiclient.discovery import build
import json
import time
from auth.credentials import YT_API_KEY

def public_service(api_key):
    service = build(serviceName='youtube', version='v3', developerKey=api_key)

    return service

def get_video_id(queries, api):
    service = public_service(api)
    ids = []
    for i in range(len(queries)):
        request = service.search().list(part='snippet',maxResults=2, q=queries[i])
        response = request.execute()
        videoid = response['items'][0]['id']['videoId']
        print(videoid)

        ids.append(videoid)

        time.sleep(3)
    
    return ids