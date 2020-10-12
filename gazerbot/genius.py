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
        if 'error' in song_data:
            return None
        else:
            return song_data["lyrics"]
    except:
        genius = lyricsgenius.Genius(secrets.GENIUS_TOKEN)
        song = genius.search_song(title, artist=artist)

        if (song and helpers.normalize(song.title) not in helpers.normalize(title)):
            err = f"MISMATCH ERROR: {song.title}"
            print(err)
            helpers.write_to_file(lyric_file, json.dumps({"error": err}), True)
            return None
        elif not song or len(song.lyrics) <= 1:
            err = f"NO LYRICS: {title}"
            print(err)
            helpers.write_to_file(lyric_file,  json.dumps({"error": err}), True)
            return None
        else:
            song.save_lyrics(lyric_file, sanitize=False, overwrite=True)
            return song.lyrics
