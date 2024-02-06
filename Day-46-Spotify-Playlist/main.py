import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

artist = []
track_uris = []
user_id = ""

travel_week = input("Which week do you want to travel to? Type the date in the following format: YYYY-MM-DD: ")
# travel_year = travel_week.split("-")[0]


# Grabs the contents of the requested website
billboard_chart = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_week}")

# Stores the website HTML in the contents variable
billboard_100 = billboard_chart.text

# Loads the website html into BS for parsing
soup = BeautifulSoup(billboard_100, "html.parser")

# Finds the first artist on the Billboard chart, and stores it in the list called "artist". As the first arist is stored in a "p" tag instead of a "span" tag
artist.append(soup.find(name="p", class_="c-tagline a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150").get_text(strip=True))
# Finds all subsequent artist, and appends them into the list "artist" in sequential order
for name in soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"):
    artist.append(name.get_text(strip=True))


# Store the scrapped song tiltles into a list called "song_titles"
song_titles = [song.get_text(strip=True) for song in soup.find(name="a", class_="c-title__link lrv-a-unstyle-link")]
for song_name in soup.find_all(name="h3",
                               class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",
                               id="title-of-a-story"):
    song_titles.append(song_name.get_text(strip=True))


# Spotify Oauth Flow
scope = "playlist-modify-private playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="<clientid goes here>",
                                               client_secret="<client secret goes here>",
                                               redirect_uri='http://example.com', scope=scope))

# Spotify UserID
user_id = sp.current_user()["id"]


# Check to ensure the playlist to be created does not already exist.
def existing_playlist_check():
    existing_users_playlist = sp.user_playlists(user_id)
    length = len(existing_users_playlist['items'])
    existing_playlist = [existing_users_playlist['items'][playlist]['name'] for playlist in range(length)]
    if f'{travel_week} Billboard 100' in existing_playlist:
        print(f"Can't create playlist, as {travel_week} Billboard 100 playlist already exist")
    else:
        print("Doing the search, and creating your playlist!!!!! :-)")
        spotify_track_search(song_titles)

# Searches the song list on Spotify, using the song name and artist as the search query. If a song is not found, prints to the console the search failure. 
# Then creates the playlist with all the found tracks
def spotify_track_search(song_list):
    for song in song_list:
        track = sp.search(q=f"{song} {artist[song_titles.index(song)]}", type="track")
        try:
            track_uris.append(track['tracks']['items'][0]['uri'])
        except IndexError:
            print(f"{song} doesn't exist on Spotify. Skipping.")
    # Creates playlist with found tracks
    create_playlist()

# Creates the playlist on Spotify, using the track uris stored in the list "track_uris"
def create_playlist():
    playlist_creation = sp.user_playlist_create(user_id, f'{travel_week} Billboard 100', public=False,
                                                collaborative=False,
                                                description=f'Top Billboard 100 songs for the week of {travel_week}')
    add_tracks = sp.playlist_add_items(playlist_creation['id'], track_uris)
    print("Playlist created successfully!")

# Program start, checks to ensure we aren't creating a duplicate playlist
existing_playlist_check()


