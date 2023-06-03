from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "e3a28fda71f846969bffee8cf048da83"
CLIENT_PASS = "b1ec8b7c64df4d9c805eb685eb54e03a"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
#                                                client_secret=CLIENT_PASS,
#                                                redirect_uri="http://example.com",
#                                                scope="user-library-read"))

sp = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,
                                 client_secret=CLIENT_PASS,
                                 redirect_uri="http://example.com/callback",
                                 scope="playlist-modify-private",
                                 show_dialog=True,
                                 cache_path="./token.txt")

print(sp.get_auth_response())




# billboard_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# URL = f'https://www.billboard.com/charts/hot-100/{billboard_date}'
# web_html = requests.get(URL).text
# soup = BeautifulSoup(web_html, "html.parser")
# song_html = soup.select("li h3")
# # print(song_html)
# song_titles = [song.text for song in song_html]
# # print(song_titles)
# clean_titles = [song_titles[i].strip() for i in range(0, len(song_titles)-1)]
# print(clean_titles)




