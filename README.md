# Spotify to YouTube Music Playlist Transfer

This script automates the transfer of a playlist from Spotify to YouTube Music.

## Features
- Fetches playlist details from Spotify.
- Searches for matching songs on YouTube Music.
- Creates a new YouTube Music playlist with the same name.
- Adds the found songs to the newly created YouTube Music playlist.

## Prerequisites
Ensure you have Python installed along with the required libraries:

```bash
pip install spotipy ytmusicapi
```

### Required Credentials
- **Spotify API Credentials**: Obtain your `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` from the [Spotify Developer Portal](https://developer.spotify.com/).
- **YouTube Music API Credentials**:
  - Generate `headers.json` by following the [ytmusicapi documentation](https://ytmusicapi.readthedocs.io/en/latest/setup.html#authentication).
  - Obtain `GOOGLE_CONSOLE_CLIENT_ID` and `GOOGLE_CONSOLE_CLIENT_SECRET` from the [Google Cloud Console](https://console.cloud.google.com/).

## Setup and Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dev2907/SpotifyToYTmusic-python.git
   cd <repo_directory>
   ```
2. **Set up authentication:**
   - Replace `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` with your credentials.
   - Ensure `headers.json` is in the same directory.
   - Replace `GOOGLE_CONSOLE_CLIENT_ID` and `GOOGLE_CONSOLE_CLIENT_SECRET` with your credentials.

3. **Run the script:**
   ```bash
   python script.py
   ```

## How It Works
- The script authenticates with Spotify and retrieves the playlist tracks.
- It searches for the corresponding songs on YouTube Music.
- A new playlist is created in YouTube Music, and the matched songs are added to it.

## Dependencies & Credits
This project relies on:
- [Spotipy](https://spotipy.readthedocs.io/) - Python library for the Spotify Web API.
- [ytmusicapi](https://ytmusicapi.readthedocs.io/) - Unofficial YouTube Music API for interacting with YouTube Music.

## Notes
- Some songs may not have an exact match on YouTube Music.
- API rate limits may impact performance, so a `time.sleep(1)` is used to prevent excessive requests.
- Ensure proper API credentials are set up before running the script.
