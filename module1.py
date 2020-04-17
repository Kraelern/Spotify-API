import requests 
import time
endpoint = "https://accounts.spotify.com/api/token"
response = requests.get(endpoint)
print(response)


