import get_id
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import pandas as pd

mainDict={"RecommendedSongs":"","RecommendedArtists":"","RecommendedGenres":""}
PasswordDict={}

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

#print three related artists for one artist
def three_related_artists(artist_ID):
    related_artists = sp.artist_related_artists(artist_ID)
    count = 0
    return_list = []
    while count <= 2:
        count += 1
        return_list.append(related_artists['artists'][count]['name'])
    return return_list[0], return_list[1], return_list[2]
        
#get top track for one artist
def top_track(artist_ID):
    artist_top_track = sp.artist_top_tracks(artist_ID)
    for track in artist_top_track['tracks'][:1]:
        return(track['name'])

#get one recommended genre for one artist
def recommended_genres(artist_ID):      
    related_artists = sp.artist_related_artists(artist_ID)
    count = 0
    genre_list = []
    while count <= 2:
        genre_list.append(related_artists['artists'][count]['genres'])
        count += 1
    genreOverlap = list(set(genre_list[0]).intersection(genre_list[1], genre_list[2]))
    return(genreOverlap[0])

#recommended artists dict
rec_artist_list = []
rec_artist_list.append(three_related_artists(user_artist_ID_1))
rec_artist_list.append(three_related_artists(user_artist_ID_2))
rec_artist_list.append(three_related_artists(user_artist_ID_3))
mainDict["RecommendedArtists"]= rec_artist_list

#recommended genre dict
rec_genre_list = []
rec_genre_list.append(recommended_genres(user_artist_ID_1))
rec_genre_list.append(recommended_genres(user_artist_ID_2))
rec_genre_list.append(recommended_genres(user_artist_ID_3))
mainDict["RecommendedGenres"]= rec_genre_list

#recommended songs dict
rec_song_list = []
rec_song_list.append(top_track(user_artist_ID_1))
rec_song_list.append(top_track(user_artist_ID_2))
rec_song_list.append(top_track(user_artist_ID_3))
mainDict["RecommendedSongs"]= rec_song_list

nav_choice = ''
while nav_choice != 'exit':
    menu_choice = ''
    menu_choice = input('\nWhat would you like to see?\n1. Three recommended songs based on your choice of artists\n2. Three recommended genres based on your choice of artists\n3. Nine recommended artists similar to your choice of artists\n')
    if menu_choice == '1':
        print(top_track(user_artist_ID_1))
        print(top_track(user_artist_ID_2))
        print(top_track(user_artist_ID_3))
        nav_choice = input('Any key to return to menu. \'exit\' to quit. >')
        
    elif menu_choice == '2':
        print(recommended_genres(user_artist_ID_1))
        print(recommended_genres(user_artist_ID_2))
        print(recommended_genres(user_artist_ID_3))
        nav_choice = input('Any key to return to menu. \'exit\' to quit. >')
        
    elif menu_choice == '3':
        print(three_related_artists(user_artist_ID_1))
        print(three_related_artists(user_artist_ID_2))
        print(three_related_artists(user_artist_ID_3))
        nav_choice = input('Any key to return to menu. \'exit\' to quit. >')
