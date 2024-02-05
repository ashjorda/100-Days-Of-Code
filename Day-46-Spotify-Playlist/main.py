import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

track_uris = []
user_id = ""

travel_year = input("Which year do you want to travel to? Type the year in the following format: YYYY: ")

# Grabs the contents of the requested website
billboard_chart = requests.get(f"https://www.billboard.com/charts/hot-100/1986-04-28")

# Stores the website HTML in the contents variable
billboard_100 = billboard_chart.text

# Loads the website html into BS for parsing
soup = BeautifulSoup(billboard_100, "html.parser")

song_titles = [song.get_text(strip=True) for song in soup.find(name="a", class_="c-title__link lrv-a-unstyle-link")]
for song_name in soup.find_all(name="h3",
                               class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",
                               id="title-of-a-story"):
    song_titles.append(song_name.get_text(strip=True))

# Spotify Oauth Flow
scope = "playlist-modify-private playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="<client_id goes here>",
                                               client_secret="<client_secrete goes here>",
                                               redirect_uri='http://example.com', scope=scope))

# Spotify UserID
user_id = sp.current_user()["id"]


# Spotify Song Search
def spotify_track_search(songs):
    for song in song_titles:
        track = sp.search(f"track: {song} year: {travel_year}", type="track")
        try:
            track_uris.append(track['tracks']['items'][0]['uri'])
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")


def create_playlist():
    playlist_creation = sp.user_playlist_create(user_id, f'{travel_year} Billboard 100', public=False,
                                                collaborative=False,
                                                description=f'Top Billboard 100 songs for the year {travel_year}')
    add_tracks = sp.playlist_add_items(playlist_creation['id'], track_uris)
    print("Playlist created successfully!")


def existing_playlist_check():
    existing_users_playlist = sp.user_playlists(user_id)
    length = len(existing_users_playlist['items'])
    existing_playlist = [existing_users_playlist['items'][playlist]['name'] for playlist in range(length)]
    if f'{travel_year} Billboard 100' in existing_playlist:
        print("Can't create playlist, as year playlist already exist")
    else:
        create_playlist()


spotify_track_search(song_titles)
existing_playlist_check()
