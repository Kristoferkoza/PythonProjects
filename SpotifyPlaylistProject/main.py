from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "3c401b5955084c53bfd0214f85927c0b"
CLIENT_SECRET = "4c91a47a7e484b15864f4c78f13cbfa9"

# date = input("Pass the time you want to travel (YYYY-MM-DD): ")
date = "2018-07-30"
year = date.strip("-")[0]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
titles = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in titles]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Krzysztof Kozakiewicz",
    )
)
user_id = sp.current_user()["id"]

song_uri = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)