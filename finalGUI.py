"""
An application that takes user input and displays either recommended songs, artists, or genres
based on this input

Attributes:
    client_credentials_manager: grants access to the spotipy api
    sp: spotipy object
"""
import tkinter as tk
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials('898c3a3775d944e2952d43a3bc4dbd55', 'ba04bb9f22c344f99ba5eb3f8e3d9981')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

"""
A class for the spotipy application 

Attirbutes:
    name (str): name of the application
"""
class Application:
  
    def __init__(self):
        """
        A method that initializes the application object
        """
        self.name = 'Spotify Recommendation Software'
    

    def get_artist_id(self,artist_name):
        """
        A method that gets artist id
        
        Args:
            artist_name(str): name of the artist
        Returns:
            artist_id(int): the spotify specific artist id
        """
        result = sp.search(artist_name)
        artist_id = result['tracks']['items'][0]['artists'][0]['id']
        return artist_id
    

    def three_related_artists(self,artist_ID):
        """
        A method that returns a list of artists related to the ones the user inputted
        
        Args:
            artist_ID(int): the spotify specific artist id
        Returns:
            return_list(list): a list of artists related to the ones the user inputted
        """
        related_artists = sp.artist_related_artists(artist_ID)
        return_list = []
        count = 0
        while count <= 2:
            return_list.append(related_artists['artists'][count]['name'])
            count += 1
        return(return_list)
    
            
    def top_track(self,artist_ID):
        """
        A method that returns the first track from a list of top tracks of an artist related to the user's input
      
        Args: 
            artist_ID (int): the spotify specific artist id
        Returns:
            track['name'](str): returns the name of the top track
        
        """
        artist_top_track = sp.artist_top_tracks(artist_ID)
        for track in artist_top_track['tracks'][:1]:
            return(track['name'])
            
    
    def recommended_genres(self,artist_ID):    
        """
        A method that recommends genres based on the user's input
        
        Args:
            artist_ID (int): the spotify specific artist id
        Returns:
            genre_list[0][0](str): returns the first genre of the first 
                                   recommended artist if no overlap is found
            genreOverlap[0](str): returns the first common genre for each recommended artist
        """  
        related_artists = sp.artist_related_artists(artist_ID)
        count = 0
        genre_list = []
        while count <= 2:
            genre_list.append(related_artists['artists'][count]['genres'])
            count += 1
        genreOverlap = list(set(genre_list[0]).intersection(genre_list[1], genre_list[2]))
        if len(genreOverlap) == 0:
            return(genre_list[0][0])
        else:
            return(genreOverlap[0])
            
    
    def submitNames(self,artist1,artist2,artist3):
        """
        A method that appends the user's names to a global list
        Args:
            artist1(str): the user's first artist
            artist2(str):the user's second artist
            artist3(str):the user's third artist
        Returns:
            artistList(list): returns the global list
        """
        global artistList
        artistList=[]
        artistList.append(artist1.get())
        artistList.append(artist2.get())
        artistList.append(artist3.get())
        return(artistList)
    

    def clear_list(self,artistlist):
        """
        A method that clears the global list
        
        Args:
            artistlist(list): the global list of user's artists
        Returns:
            artistList(list): returns the global list of user's artists
        """
        global artistList
        artistList.clear()
        return artistList
    

    def mainWindow(self):
        """
        A method that creates the first window 
        """
        global form
        form = tk.Tk()
        form.title("Spotify Recommendation Program")
        form.configure(bg='black')
        w = 350
        h = 250
        ws = form.winfo_screenwidth()
        hs = form.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        form.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        artist1Label = tk.Label(form, text="Enter First Artist:")
        artist1Label.config(bg="black",foreground="green")
        artist1Entry = tk.Entry(form)
        artist2Label = tk.Label(form, text="Enter Second Artist:")
        artist2Label.config(bg="black",foreground="green")
        artist2Entry = tk.Entry(form)
        artist3Label = tk.Label(form, text="Enter Third Artist:")
        artist3Label.config(bg="black",foreground="green")
        artist3Entry = tk.Entry(form)

        artist1Label.grid(row=0, column=0,padx=15, pady=15)
        artist1Entry.grid(row=0, column=1,padx=15, pady=15)
                
        artist2Label.grid(row=1, column=0,padx=15, pady=15)
        artist2Entry.grid(row=1, column=1,padx=15, pady=15)
                
        artist3Label.grid(row=2, column=0,padx=15, pady=15)
        artist3Entry.grid(row=2, column=1,padx=15, pady=15)

        btnSubmit = tk.Button(form, text="Submit",command=lambda:[self.submitNames(artist1Entry,artist2Entry,artist3Entry), self.menuWindow()])
        btnSubmit.config(background="black",foreground="green")
        btnSubmit.grid(columnspan=2, padx=15, pady=15)

        form.mainloop()
    

    def menuWindow(self):
        """
        A method that creates the menu window
        """
        window2 = tk.Toplevel(form)
        window2.title("Options Menu")
        window2.configure(bg='black')
        w = 350
        h = 250
        ws = window2.winfo_screenwidth()
        hs = window2.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window2.geometry('%dx%d+%d+%d' % (w, h, x, y))

        btnSubmit1 = tk.Button(window2, text="Display Recommended Artists",command =lambda: [self.artistWindow(self.three_related_artists(self.get_artist_id(artistList[0])),
                                                                                                              self.three_related_artists(self.get_artist_id(artistList[1])),
                                                                                                              self.three_related_artists(self.get_artist_id(artistList[2])))])
        btnSubmit1.config(background="black",foreground="green")
        btnSubmit1.grid(columnspan=2, padx=15, pady=15)

        btnSubmit2 = tk.Button(window2, text="Display Recommended Songs",command =lambda: [self.songWindow(self.top_track(self.get_artist_id(self.three_related_artists(self.get_artist_id(artistList[0]))[0])),
                                                                                                          self.top_track(self.get_artist_id(self.three_related_artists(self.get_artist_id(artistList[1]))[0])),
                                                                                                          self.top_track(self.get_artist_id(self.three_related_artists(self.get_artist_id(artistList[2]))[0])))])
        btnSubmit2.config(background="black",foreground="green")
        btnSubmit2.grid(columnspan=4, padx=15, pady=15)
        
        btnSubmit3 = tk.Button(window2, text="Display Recommended Genres",command =lambda: [self.genreWindow(self.recommended_genres(self.get_artist_id(artistList[0])),
                                                                                                            self.recommended_genres(self.get_artist_id(artistList[1])),
                                                                                                            self.recommended_genres(self.get_artist_id(artistList[2])))])
        btnSubmit3.config(background="black",foreground="green")
        btnSubmit3.grid(columnspan=6, padx=15, pady=15)
        
        backButton4 = tk.Button(window2, text= 'Back', command = lambda: [self.mainWindow(), self.clear_list(artistList)])
        backButton4.config(background="black",foreground="red")
        backButton4.grid(columnspan = 8, padx = 15, pady = 15)

        window2.mainloop()
        
        
    def artistWindow(self, artists1, artists2, artists3):
        """
        A method that creates the artist window
        
        Args:
            artist1(str): the first three recommended artists
            artist2(str): the next three recommended artists
            artist3(str): the last three recommended artist
        """
        window3 = tk.Toplevel(form)
        window3.title("Artist Menu")
        window3.configure(bg='black')
        w = 350
        h = 250
        ws = window3.winfo_screenwidth()
        hs = window3.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window3.geometry('%dx%d+%d+%d' % (w, h, x, y))

        outputBox = tk.Label(window3)
        outputBox.grid(columnspan=2, padx=15, pady=15)
        
        outputBox2 = tk.Label(window3)
        outputBox2.grid(columnspan=3, padx=15, pady=15)
        
        outputBox3 = tk.Label(window3)
        outputBox3.grid(columnspan=4, padx=15, pady=15)
        
        outputBox['text'] = artists1[0] + "\n" + artists1[1] + "\n" + artists1[2]
        outputBox2['text'] = artists2[0] + "\n" + artists2[1] + "\n" + artists2[2]
        outputBox3['text'] = artists3[0] + "\n" + artists3[1] + "\n" + artists3[2]
        
        backButton = tk.Button(window3, text= 'Back', command = lambda: [self.menuWindow()])
        backButton.grid(columnspan = 8, padx = 15, pady = 15)

        window3.mainloop()
        
        
    def songWindow(self,song1, song2, song3):
        """
        A method that creates the song window
        
        Args:
            song1(str): the first recommended song
            song2(str): the next recommended song
            song3(str): the last recommended song
        """
        window4 = tk.Toplevel(form)
        window4.title("Song Menu")
        window4.configure(bg='black')
        w = 350
        h = 250
        ws = window4.winfo_screenwidth()
        hs = window4.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window4.geometry('%dx%d+%d+%d' % (w, h, x, y))

        outputBox = tk.Label(window4)
        outputBox.grid(columnspan=2, padx=15, pady=15)
        
        outputBox2 = tk.Label(window4)
        outputBox2.grid(columnspan=3, padx=15, pady=15)
        
        outputBox3 = tk.Label(window4)
        outputBox3.grid(columnspan=4, padx=15, pady=15)
        
        outputBox['text'] = song1
        outputBox2['text'] = song2
        outputBox3['text'] = song3
        
        backButton = tk.Button(window4, text= 'Back', command = lambda: [self.menuWindow()])
        backButton.grid(columnspan = 8, padx = 15, pady = 15)
        
        window4.mainloop()
        
        
    def genreWindow(self,genre1, genre2, genre3):
        """
        A method that creates the genre window
        
        Args:
            genre1(str): the first recommended genre
            genre2(str): the second recommended genre
            genre3(str): the third recommended genre
        """
        window5 = tk.Toplevel(form)
        window5.configure(bg='black')
        form.title("Genre Menu")
        w = 350
        h = 250
        ws = window5.winfo_screenwidth()
        hs = window5.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window5.geometry('%dx%d+%d+%d' % (w, h, x, y))

        outputBox = tk.Label(window5)
        outputBox.grid(columnspan=2, padx=15, pady=15)
        
        outputBox2 = tk.Label(window5)
        outputBox2.grid(columnspan=3, padx=15, pady=15)
        
        outputBox3 = tk.Label(window5)
        outputBox3.grid(columnspan=4, padx=15, pady=15)
        
        outputBox['text'] = genre1
        outputBox2['text'] = genre2
        outputBox3['text'] = genre3
        
        backButton = tk.Button(window5, text= 'Back', command = lambda: [self.menuWindow()])
        backButton.grid(columnspan = 8, padx = 15, pady = 15)
        
        window5.mainloop()


if __name__ == '__main__':
    spot_app = Application()
    spot_app.mainWindow()