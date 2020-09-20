import lyricsgenius
import re
import json
from gazerbot import secrets, helpers

def get_lyrics(artist, title):
    lyric_file = f"lyrics/db/{helpers.normalize(artist+title)}.json"
    try:
        f = open(lyric_file, "r") # already downloaded lyrics
        song_data = json.load(f)
        f.close()
        return song_data["lyrics"]
    except:
        genius = lyricsgenius.Genius(secrets.GENIUS_TOKEN)
        song = genius.search_song(title, artist=artist)

        if (song and helpers.normalize(song.title) not in helpers.normalize(title)):
            print(f"MISMATCH ERROR: {song.title}")
            return None
        elif not song or len(song.lyrics) <= 1:
            print(f"NO LYRICS: {title}")
            return None
        else:
            song.save_lyrics(lyric_file, sanitize=False, overwrite=True)
            return song.lyrics
