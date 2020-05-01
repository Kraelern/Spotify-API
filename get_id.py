import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getArtist_id(artist_name):
    result = sp.search(artist_name)
    artist_id = result['tracks']['items'][0]['artists'][0]["id"]
    return artist_id
    
def getAlbum_id(album_name):
    result = sp.search(album_name)
    album_id = result['tracks']['items']
    return album_id
    
#def get_song_id(song_name):
song_name = input('song name: ')
result = sp.search(song_name)
song_id = result
print(song_id)
