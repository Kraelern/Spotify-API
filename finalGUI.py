import tkinter as tk
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artistList=[]

def submitNames(artist1,artist2,artist3):
    global artistList
    artistList.append(artist1.get())
    artistList.append(artist2.get())
    artistList.append(artist3.get())
    return(artistList) 

def get_artist_id(artist_name):
    result = sp.search(artist_name)
    artist_id = result['tracks']['items'][0]['artists'][0]['id']
    return artist_id

def three_related_artists(artist_ID):
    related_artists = sp.artist_related_artists(artist_ID)
    count = 0
    while count <= 2:
        print(related_artists['artists'][count]['name'])
        count += 1
        
#get top track for one artist
def top_track(artist_ID):
    artist_top_track = sp.artist_top_tracks(artist_ID)
    for track in artist_top_track['tracks'][:1]:
        print(track['name'])
        
#get one recommended genre for one artist
def recommended_genres(artist_ID):      
    related_artists = sp.artist_related_artists(artist_ID)
    count = 0
    genre_list = []
    while count <= 2:
        genre_list.append(related_artists['artists'][count]['genres'])
        count += 1
    genreOverlap = list(set(genre_list[0]).intersection(genre_list[1], genre_list[2]))
    if len(genreOverlap) == 0:
        print(genre_list[0][0])
    else:
        print(genreOverlap[0])
    
def getUserArtistID(artist1,artist2,artist3):
    #turning the user_artist_list from a string into the IDs
    user_artist_ID_1 = get_artist_id(artist1)
    user_artist_ID_2 = get_artist_id(artist2)
    user_artist_ID_3 = get_artist_id(artist3)
    return user_artist_ID_1,user_artist_ID_2, user_artist_ID_3

def newWindow():
   # newwin = tk.Toplevel()
    form = tk.Tk()
    form.title("Options Menu")



    btnSubmit = tk.Button(form, text="Display Recommended Artists",command =lambda: [three_related_artists(get_artist_id(artistList[0])),three_related_artists(get_artist_id(artistList[1])),three_related_artists(get_artist_id(artistList[2]))])
    btnSubmit.grid(columnspan=2, padx=15, pady=15)

    btnSubmit = tk.Button(form, text="Display Recommended Songs",command =lambda: [top_track(get_artist_id(artistList[0])),top_track(get_artist_id(artistList[1])),top_track(get_artist_id(artistList[2]))])
    btnSubmit.grid(columnspan=4, padx=15, pady=15)
    
    btnSubmit = tk.Button(form, text="Display Recommended Genres",command =lambda: [recommended_genres(get_artist_id(artistList[0])),recommended_genres(get_artist_id(artistList[1])),recommended_genres(get_artist_id(artistList[2]))])
    btnSubmit.grid(columnspan=6, padx=15, pady=15)

    form.mainloop()

form = tk.Tk()
form.title("Spotify Recommendation Program")
artist1Label = tk.Label(form, text="Enter First Artist:")
artist1Entry = tk.Entry(form)
artist2Label = tk.Label(form, text="Enter Second Artist:")
artist2Entry = tk.Entry(form)
artist3Label = tk.Label(form, text="Enter Third Artist:")
artist3Entry = tk.Entry(form)

artist1Label.grid(row=0, column=0,padx=15, pady=15)
artist1Entry.grid(row=0, column=1,padx=15, pady=15)
    
artist2Label.grid(row=1, column=0,padx=15, pady=15)
artist2Entry.grid(row=1, column=1,padx=15, pady=15)
    
artist3Label.grid(row=2, column=0,padx=15, pady=15)
artist3Entry.grid(row=2, column=1,padx=15, pady=15)

btnSubmit = tk.Button(form, text="Submit",command=lambda:[submitNames(artist1Entry,artist2Entry,artist3Entry), newWindow()])
btnSubmit.grid(columnspan=2, padx=15, pady=15)

form.mainloop()