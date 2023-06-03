import json

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "e3a28fda71f846969bffee8cf048da83"
CLIENT_PASS = "b1ec8b7c64df4d9c805eb685eb54e03a"
#TOKEN = "AQDB2DqabL-sQKuZbZW-r5V2M3G81qgZx5lbAu-waJoDDIUtcgAROnD8PD10qDUn_B-_ZXxI2Do5o0GwgxCQ1O8Yk6jwbX--eSHWv_wr8GwHD8HRUE2ej0G6_5qp2nligmBjWL7SjUU7KKEvdn1ELvj0zu2lGLhdhSXP9y1lRpKC3Xc7tupYA-ml9Jv3mPbxHoB6GQcxAdmn"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
#                                                client_secret=CLIENT_PASS,
#                                                redirect_uri="http://example.com",
#                                                scope="user-library-read"))

# sp = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,
#                                  client_secret=CLIENT_PASS,
#                                  redirect_uri="http://example.com/callback/",
#                                  scope="playlist-modify-private",
#                                  )
#
# print(sp.get_auth_response())

# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com/callback/",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_PASS,
#         show_dialog=True,
#         cache_path="./token.txt"
#     )
# )
# user_id = sp.current_user()
# print(json.dump(user_id, sort_keys=True, indent=4))




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




