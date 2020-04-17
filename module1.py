import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '898c3a3775d944e2952d43a3bc4dbd55'
secret = 'ba04bb9f22c344f99ba5eb3f8e3d9981'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)
