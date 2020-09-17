import lyricsgenius
import re
from gazerbot import secrets, helpers

def get_lyrics(artist, title):
    genius = lyricsgenius.Genius(secrets.GENIUS_TOKEN)
    song = genius.search_song(title, artist=artist)

    if (song and helpers.normalize(song.title) not in helpers.normalize(title)):
        print(f"MISMATCH ERROR: {song.title}")
        return None
    elif not song or len(song.lyrics) <= 1:
        print(f"NO LYRICS: {title}")
        return None
    else:
        song.save_lyrics(f"lyrics/db/{helpers.normalize(artist+title)}", sanitize=False, overwrite=True)
        return song.lyrics
