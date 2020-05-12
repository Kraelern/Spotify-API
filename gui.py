import tkinter as tk
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
HEIGHT = 500
WIDTH = 600

def get_artist_id(artist_name1,artist_name2,artist_name3):
    result1 = sp.search(artist_name1)
    artist_id1 = result1['tracks']['items'][0]['artists'][0]['id']
    result2 = sp.search(artist_name2)
    artist_id2 = result2['tracks']['items'][0]['artists'][0]['id']
    result3 = sp.search(artist_name3)
    artist_id3 = result3['tracks']['items'][0]['artists'][0]['id']
    #return artist_id
    label['text'] = artist_id1
    label['text'] = artist_id2
    label['text'] = artist_id3

def get_album_id(album_name):
    result = sp.search(album_name)
    album_id = result['tracks']['items'][0]['album']
    return album_id

def three_related_artists(artist_ID):
    related_artists = sp.artist_related_artists(artist_ID)
    count = 0
    while count <= 2:
        #print(related_artists['artists'][count]['name'])
        label['text'] = related_artists['artists'][count]['name']
        count += 1
        
#get top track for one artist
def top_track(artist_ID):
    artist_top_track = sp.artist_top_tracks(artist_ID)
    for track in artist_top_track['tracks'][:1]:
        #return(track['name'])
        label['text'] = track['name']
#get one recommended genre for one artist
def recommended_genres(artist_ID):      
    related_artists = sp.artist_related_artists(artist_ID)
    count = 0
    genre_list = []
    while count <= 2:
        genre_list.append(related_artists['artists'][count]['genres'])
        count += 1
    genreOverlap = list(set(genre_list[0]).intersection(genre_list[1], genre_list[2]))
    #return(genreOverlap[0])
    label['text'] =genreOverlap[0]
    
#def getUserArtists(artist1,artist2,artist3):
    #getting the users three artists and appending them into a list
    #user_artist_one = artist1
    #user_artist_two = artist2
    #user_artist_three = artist3
    #user_artist_list = []
    #user_artist_list.append(user_artist_one)
    #user_artist_list.append(user_artist_two)
    #user_artist_list.append(user_artist_three)
    #return user_artist_one, user_artist_two, user_artist_three
    
def getUserArtistID(artist1,artist2,artist3):
    #turning the user_artist_list from a string into the IDs
    user_artist_ID_1 = get_artist_id(artist1,artist2,artist3)
    #user_artist_IDs = []
    #user_artist_IDs.append(user_artist_ID_1)
    #user_artist_IDs.append(user_artist_ID_2)
    #user_artist_IDs.append(user_artist_ID_3)
    return user_artist_ID_1
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry1 = tk.Entry(frame, font=40)
entry1.place(relx=0.1,rely=0.5,relwidth=0.3, relheight=0.4)

entry2 = tk.Entry(frame, font=40)
entry2.place(relx=0.3,rely=0.7,relwidth=0.3, relheight=0.4)

entry3 = tk.Entry(frame, font=40)
entry3.place(relx=0.5,rely=0.9,relwidth=0.3, relheight=0.4)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda:getUserArtistID(entry1.get(),entry2.get(),entry3.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
