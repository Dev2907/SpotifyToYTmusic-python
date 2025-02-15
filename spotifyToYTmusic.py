import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic, OAuthCredentials
import time

SPOTIFY_CLIENT_ID = 'GET YOUR CREDENTIALS'
SPOTIFY_CLIENT_SECRET = 'GET YOUR CREDENTIALS'
GOOGLE_CONSOLE_CLIENT_id = "GET YOUR CREDENTIALS"
GOOGLE_CONSOLE_CLIENT_SECRET = "GET YOUR CREDENTIALS"


sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    )
)

# YouTube Music Authentication
ytmusic = YTMusic("headers.json", oauth_credentials=OAuthCredentials(client_id=GOOGLE_CONSOLE_CLIENT_id, client_secret=GOOGLE_CONSOLE_CLIENT_SECRET))

def fetch_playlist_spotify(api, playlist_id):
    response = api.playlist_tracks(playlist_id, limit=100, offset=0)  # Fetch first batch
    playlist_name = api.playlist(playlist_id)["name"]  # Get playlist name
    
    tracks = []
    
    while response:  # Loop through pages
        for item in response["items"]:
            track_name = item["track"]["name"]
            artist_name = item["track"]["artists"][0]["name"]
            tracks.append(f"{track_name} {artist_name}")

        if response["next"]:  # If there is a next page
            response = api.next(response)
        else:
            break  # No more pages

    return playlist_name, tracks

def get_videoID_YTMusic(queries):
    video_ids = []
    for query in queries:
        search_results = ytmusic.search(query, filter="songs")
        if search_results:
            video_ids.append(search_results[0]['videoId'])
        time.sleep(1)  # Avoid excessive requests
    return video_ids

def make_playlist_YTMusic(name):
    playlist_id = ytmusic.create_playlist(name, "Created via script", privacy_status="PUBLIC")
    return playlist_id

def add_to_playlist_YTMusic(playlist_id, video_ids):
    ytmusic.add_playlist_items(playlist_id, video_ids, duplicates=True)

if __name__ == "__main__":
    spotify_playlist_id = ""  # Your Spotify playlist ID
    name, queries = fetch_playlist_spotify(sp, spotify_playlist_id)

    
    print(f"Spotify Playlist Name: {name}")
    YTPlaylistID = make_playlist_YTMusic(name)
    print(f"Created YT Music playlist with ID: {YTPlaylistID}")
    
    video_ids = get_videoID_YTMusic(queries)
    add_to_playlist_YTMusic(YTPlaylistID, video_ids)
    print("Done")



