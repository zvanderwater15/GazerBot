import lyricsgenius
import re
import json
from gazerbot import api_secrets, helpers
import os
import sys

def sanitize_lyrics(lyrics):
    # each line starts with "song title" "lyrics", so remove these words
    sans_title = lyrics[lyrics.index('\n') + 1:] if '\n' in lyrics else lyrics
    # remove Embed or 1embed  or {num}embed at the end of each song
    sans_recommendation = sans_title.lower().replace("you might also like", "")
    sans_embed = re.sub(r'([0-9]|[1-9][0-9])?embed', '', sans_recommendation)
    return sans_embed

class Song:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.file = f"lyrics/db/{helpers.normalize(self.artist+self.title)}.json"
        self.lyrics = None
    
    def __str__(self):
        return f"{self.artist}-{self.title}"

    def get_lyrics(self, genius):
        if self.lyrics:
            return self.lyrics

        lyrics = self._load_from_file()
        if not lyrics:
            lyrics = genius.get_lyrics(self.artist, self.title, self.file)

        if lyrics:
            self.lyrics = sanitize_lyrics(lyrics)
        else:
            self.lyrics = None

        return self.lyrics
       
    def _load_from_file(self):
        # print("lyrics from..", os.path.abspath(os.path.join(os.path.dirname(__file__))))
        try:
            f = open(self.file, "r") # already downloaded lyrics
        except OSError as e:
            print(f"{type(e)}: {e}", file=sys.stderr)
            return None
            
        try:
            song_data = json.load(f)
        except:
            print(f"song data stored incorrectly for {self.file}, rewriting", file=sys.stderr)
            song_data = None
        finally:
            f.close()

        # currently ignore errors to redownload songs in case it was due to a past programmatic error
        if not song_data or 'error' in song_data:
            return None 
        else:
            return song_data.get("lyrics")


class Genius:
    def __init__(self):
        self.genius = lyricsgenius.Genius(api_secrets.GENIUS_TOKEN)
        self.genius.remove_section_headers = True

    def get_lyrics(self, artist, title, save_file):
        song = self.genius.search_song(title, artist=artist)
        err = None
        if song and helpers.normalize(song.title) not in helpers.normalize(title):
            err = f"MISMATCH ERROR: {song.title}"
        elif not song or len(song.lyrics) <= 1:
            err = f"NO LYRICS: {title}"
        print(save_file)
        if err:
            helpers.write_to_file(save_file, json.dumps({"error": err}), True)
            return None
        else:
            song.save_lyrics(save_file, sanitize=False, overwrite=True)
            return song.lyrics
