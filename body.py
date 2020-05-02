import get_id
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#user_choice = input('What would you like to do? Enter a number:\n1. ')
mydict = {}
output = get_id.get_album_id('Graduation')
for key in output[1]:
    c = output[1]['id']
    mydict[c] = mydict.get(c, 0) + 1
print(mydict)