def extract_data(api, items):
    tracks_data = []
    for i in items:
        item = dict.fromkeys(['track_name','artist_name','album_name'])
        track_name = i['track']['name']
        artist_name = i['track']['artists'][0]['name']
        album_name = i['track']['album']['name']

        item['track_name'] = track_name
        item['artist_name'] = artist_name
        item['album_name'] = album_name

        tracks_data.append(item)
    return tracks_data

def query_builder(playlist_data):
    queries = []
    for obj in playlist_data:
        q = "{} {} {}".format(obj['track_name'],obj['album_name'],obj['artist_name'])
        queries.append(q)
    return queries
    