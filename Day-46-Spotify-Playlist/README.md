# Billboard Top 100 Playlist Creator

This Python script allows you to create a Spotify playlist containing the top Billboard 100 songs for a specific week. It scrapes the Billboard website for the top songs of the specified week, searches for these songs on Spotify, and creates a playlist with the found tracks.

## Prerequisites

Before running the script, make sure you have the following installed:

- `Python 3.x`
- `requests`
- `spotipy`
- `beautifulsoup4`

You can install these dependencies via pip: 
```
pip install requests spotipy beautifulsoup4
``````

## Usage

1. Replace `<clientid goes here>` and `<client secret goes here>` in the script on line 40, and 41 with your Spotify API client ID and client secret. You can obtain these by creating a Spotify Developer account and registering your application.

3. Run the script:

```
python billboard_playlist_creator.py
```

4. Follow the prompts and input the date of the week you want to create a playlist for in the format `YYYY-MM-DD`.

5. The script will then search for the top Billboard 100 songs for that week and create a Spotify playlist with the found tracks.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ashjorda/100-Days-Of-Code/blob/master/LICENSE) file for details.
