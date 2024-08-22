import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# scraping the billboard100 website
URL = os.environ["SITE_URL"]
date = input("What year would you like to travel to? Type the date in this format: YYYY-MM-DD\n")
response = requests.get(URL + date)
billboard100 = response.text

soup = BeautifulSoup(billboard100, "html.parser")
songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in songs]

# Spotipy authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["CLIENT_ID"],
                                               client_secret=os.environ["CLIENT_SECRET"],
                                               redirect_uri=os.environ["REDIRECT_URI"],
                                               scope=os.environ["PLAYLIST_SCOPE"],
                                               requests_timeout=20))

# get user_id
user_id = sp.current_user()["id"]

# create the spotify song uris
song_uris = []
for song in song_names:
    # use a try except block to catch any errors
    try:
        result = sp.search(q=f"track:{song}", type="track", limit=1)

        if result["tracks"]["items"]:
            track = result["tracks"]["items"][0]
            song_uris.append(track["uri"])
        else:
            print(f"No track found for this {song}")
    except Exception as e:
        print(f"Error searching for {song}: {e}")

# Create a playlist
playlist = sp.user_playlist_create(user=os.environ["USER_ID"],
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   collaborative=False,
                                   description=f"BillBoard 100 on {date}")

songs_in_playlist = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(songs_in_playlist)
