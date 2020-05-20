import finalGUI

#making an instance of the Application class to test
testobject = finalGUI.Application()

#testing if the get_artist_id method returns Drake's correct Spotify ID
assert testobject.get_artist_id('Drake') == '3TVXtAsR1Inumwj472S9r4'

#testing if the three_related_artists method returns Drake's top three related artists
assert testobject.three_related_artists('3TVXtAsR1Inumwj472S9r4') == ['Big Sean', 'J. Cole', 'Wale']


assert testobject.top_track