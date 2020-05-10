import get_id
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#getting the users three artists and appending them into a list
user_artist_one = input('Enter three artists: \n1: ')
user_artist_two = input('Enter a second artist: \n2: ')
user_artist_three = input('Enter the third artist: \n3: ')
user_artist_list = []
user_artist_list.append(user_artist_one)
user_artist_list.append(user_artist_two)
user_artist_list.append(user_artist_three)

#turning the user_artist_list from a string into the IDs
user_artist_ID_1 = get_id.get_artist_id(user_artist_one)
user_artist_ID_2 = get_id.get_artist_id(user_artist_two)
user_artist_ID_3 = get_id.get_artist_id(user_artist_three)
user_artist_IDs = []
user_artist_IDs.append(user_artist_ID_1)
user_artist_IDs.append(user_artist_ID_2)
user_artist_IDs.append(user_artist_ID_3)

#get three related artists for each artist
def three_related_artists(artist_ID):
    related_artists = sp.artist_related_artists(artist_ID)
    count = 0
    while count <= 2:
        print(related_artists['artists'][count]['name'])
        count += 1

#finds and recommends three genres based on user input
def recommended_genres(artist_ID_1):      
    related_artists = sp.artist_related_artists(artist_ID_1)
    count = 0
    genre_list = []
    while count<=2:
        genre_list.append(related_artists['artists'][count]['genres'])
        count+=1
    genreOverlap = list(set(genre_list[0]).intersection(genre_list[1],genre_list[2]))
    print(genreOverlap[0])
            
        
three_related_artists(user_artist_ID_1)
three_related_artists(user_artist_ID_2)
three_related_artists(user_artist_ID_3)

recommended_genres(user_artist_ID_1)
recommended_genres(user_artist_ID_2)
recommended_genres(user_artist_ID_3)

