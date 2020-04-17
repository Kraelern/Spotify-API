import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
cid ="898c3a3775d944e2952d43a3bc4dbd55" 
secret = "ba04bb9f22c344f99ba5eb3f8e3d9981"
username = "the_ranaga"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
