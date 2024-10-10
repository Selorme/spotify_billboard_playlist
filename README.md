# Billboard 100 Playlist Generator 🎶

This Python script allows you to create a Spotify playlist featuring the Billboard Top 100 songs for a specific date. It scrapes the Billboard website for song names and uses the Spotify API to search for the corresponding tracks and create a playlist on your Spotify account.

## Features
- Scrapes the Billboard 100 songs for a specific date (input by the user).
- Uses the Spotify API to search for songs and add them to a newly created playlist.
- Automates playlist creation with Spotipy and Spotify API.

## Requirements
- Python 3.8+
- Spotify Developer Account
- Spotipy (Spotify API library)
- BeautifulSoup (for web scraping)
- Requests (for making HTTP requests)
- dotenv (to load environment variables)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Selorme/spotify_billboard_playlist.git
   cd billboard-playlist-generator
   ```

2. **Set up a virtual environment** (optional, but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root of the project and add the following variables:

     ```env
     CLIENT_ID=your_spotify_client_id
     CLIENT_SECRET=your_spotify_client_secret
     REDIRECT_URI=http://localhost:8888/callback
     PLAYLIST_SCOPE=playlist-modify-private
     SITE_URL=https://www.billboard.com/charts/hot-100/
     USER_ID=your_spotify_user_id
     ```

   - Get your Spotify API credentials by [registering a new application](https://developer.spotify.com/dashboard/applications).

5. **Run the script**:
   ```bash
   python main.py
   ```

   The script will prompt you to enter a date in the format `YYYY-MM-DD`, and it will create a Spotify playlist based on the Billboard Hot 100 songs for that date.

## How It Works

1. **Billboard Scraping**: 
   - The script uses the `requests` library to fetch Billboard's top 100 page for the given date and `BeautifulSoup` to extract the song titles.

2. **Spotify Authentication**:
   - It uses Spotipy to authenticate with Spotify using the Spotify OAuth flow (via `SpotifyOAuth`). The authentication requires your `client_id`, `client_secret`, and `redirect_uri`.

3. **Spotify Playlist Creation**:
   - The script searches for each song using Spotify's search API and collects the song URIs.
   - Finally, it creates a playlist and adds the songs to it.

## Example Usage

```bash
$ python main.py
What year would you like to travel to? Type the date in this format: YYYY-MM-DD
1985-07-20
```

After running the script, a playlist named `1985-07-20 Billboard 100` will be created in your Spotify account.

## Dependencies

- `spotipy`: Spotify API integration.
- `requests`: HTTP library for making requests to the Billboard website.
- `beautifulsoup4`: For scraping song names from the Billboard charts.
- `python-dotenv`: For managing environment variables.

## License

This project is licensed under the MIT License.

---

Feel free to contribute, open issues, or fork the project to customize it further! 