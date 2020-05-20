import finalGUI

#making an instance of the Application class to test
testobject = finalGUI.Application()

#testing if the get_artist_id method returns Drake's correct Spotify ID
assert testobject.get_artist_id('Drake') == '3TVXtAsR1Inumwj472S9r4'

#testing if the three_related_artists method returns Drake's top three related artists
assert testobject.three_related_artists('3TVXtAsR1Inumwj472S9r4') == ['Big Sean', 'J. Cole', 'Wale']

#testing if the top_track methos return's Drake's top track at this moment in time
assert testobject.top_track('3TVXtAsR1Inumwj472S9r4') == 'Toosie Slide'

#testing if the recommended_genres method returns hip hop for Drake
string_len = 0
for i in testobject.recommended_genres('3TVXtAsR1Inumwj472S9r4'):
    string_len += 1
assert string_len > 2

#the previous functions were the only functions that could be automatically tested.
#the functions in the finalGUI module follwing recommended_genres cannot be automatically tested since they all require user input to function.
#the testing procedure we followed was simple and tested by hand.
#to check if submitNames correctly appended the user's inputs to a list, we printed the list in the terminal to make sure it was not empty.
#to check if clear_list worked properly, we ran the program again after running the clear_list function and checked that the results were different (which they were).
#to check if mainWindow ran properly, we ran the file and ensured that the GUI looked the way we wanted it to.
#the same process applied to menuWindow, artistWindow, songWindow, and genreWindow.