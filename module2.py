import sys
import spotipy
import spotipy.util as util

util.prompt_for_user_token(username= 'the_ranaga',
                           scope= 'user-library-read',
                           client_id= '898c3a3775d944e2952d43a3bc4dbd55',
                           client_secret= 'ba04bb9f22c344f99ba5eb3f8e3d9981',
                           redirect_uri= 'http://localhost/')

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)
