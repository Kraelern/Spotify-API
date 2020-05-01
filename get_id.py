import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getArtist_id(artist_name):
    #name = input("enter an artist name: ")
    result = sp.search(artist_name) 
    artist_id = result['tracks']['items'][0]['artists'][0]["id"]
    #print(sp.artist_related_artists(artist_id))
    
#def getAlbum_id():
album_name = input("enter an album name: ") 
result = sp.search(album_name)
album_id = result['tracks']['items']
print(album_id)