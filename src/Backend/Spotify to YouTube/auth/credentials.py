from pathlib import Path

file_path = Path(__file__).parent.absolute()


SP_CLIENT_ID = '7971666e36d24b74a2a83b33268a7372'
SP_CLIENT_SECRET = '7db152d100ad4c63a99ec22c3273480c'
SP_REDIRECT_URI = 'https://www.github.com/upes-open/OMusigator'
YT_API_KEY = 'AIzaSyDbOM4zQ039gIhtdHDgs4D3ZxXijGOKh0s'

YOUTUBE_SECRETS = file_path / Path("auth/client_secrets.json")