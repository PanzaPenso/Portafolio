from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "e3a28fda71f846969bffee8cf048da83"
CLIENT_PASS = "b1ec8b7c64df4d9c805eb685eb54e03a"

# sp = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,
#                                  client_secret=CLIENT_PASS,
#                                  redirect_uri="http://example.com/callback/",
#                                  scope="playlist-modify-private",
#                                  )
#
# print(sp.get_auth_response())
# print(sp.get_cached_token())

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private user-follow-read playlist-read-private",
        redirect_uri="http://example.com/callback/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_PASS,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
billboard_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f'https://www.billboard.com/charts/hot-100/{billboard_date}'
web_html = requests.get(URL).text
soup = BeautifulSoup(web_html, "html.parser")
song_html = soup.select("li h3")

song_titles = [song.text for song in song_html]
clean_titles = [song_titles[i].strip() for i in range(0, len(song_titles)-1)]

year = billboard_date.split("-")[0]
# print(year)
playlist = sp.user_playlist_create(user_id, f"{billboard_date}-Billboard_100", public=False, description='QUE FUNCIONE ESTA CHIMBADA!!!')
song_uris = []
# print(clean_titles)
for songs in clean_titles:
    result = sp.search(q=f"track:{songs} year:{year}", type="track", limit=1)
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{songs} doesn't exist in Spotify. Skipped.")

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris[:100])
print("\n")
print("GAME OVER")



