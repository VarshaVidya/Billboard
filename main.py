import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
# year = input("Which year do you want to "
#              "travel to ? Type the date in this format "
#              "YYYY-MM-DD:")
response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
billboard = response.text
soup = BeautifulSoup(billboard,"html.parser")
songs_100 = soup.select("li ul li h3")
names = [song.getText().strip() for song in songs_100]
print(names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id="def68398370c4913a3bdef3dc2de4f7b",
        client_secret="f483b30ea1454e87bdc2753fa36bf556",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


