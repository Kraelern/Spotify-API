import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import get_id

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#get first album search result id
output = get_id.get_album_id('Graduation')
albumdict = {}
for key in output:
    c = output['id']
    albumdict[c] = albumdict.get(c)
print(str(next(iter(albumdict))))

#get artist id
output2 = get_id.get_artist_id('Illenium')
print(output2)

#getting artist_related_artists to work
related_artists = sp.artist_related_artists('69GGBxA162lTqCwzJG5jLp')#Illenium
print(related_artists['artists'][0]['name'])

#getting top three artist_related_artists to return
related_artists = sp.artist_related_artists('69GGBxA162lTqCwzJG5jLp')#Illenium
count = 0
while count <= 2:
    print(related_artists['artists'][count]['name'])
    count += 1
