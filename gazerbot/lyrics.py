import lyricsgenius
import re
import json
from gazerbot import api_secrets, helpers
import os
import sys

class LyricError(Exception):
    pass

def sanitize_lyrics(lyrics):
    # each line starts with "song title" "lyrics", so remove these words
    sans_title = lyrics[lyrics.index('\n') + 1:] if '\n' in lyrics else lyrics
    # remove Embed or 1embed  or {num}embed at the end of each song
    sans_recommendation = sans_title.lower().replace("you might also like", "")
    sans_embed = re.sub(r'([0-9]|[1-9][0-9])?embed', '', sans_recommendation)
    return sans_embed

class Song:
    def __init__(self, db, artist, title):
        self.artist = artist
        self.title = title
        self.db = db
        self.lyrics = None
    
    def __str__(self):
        return f"{self.artist}-{self.title}"

    def get_lyrics(self, genius):
        if self.lyrics:
            return self.lyrics

        track = self.db.get_track(self.artist, self.title)
        if track and not track["error"]:
            self.lyrics = track["content"]
        else:
            try:
                self.lyrics = genius.get_lyrics(self.artist, self.title)
                self.lyrics = sanitize_lyrics(self.lyrics)
                self.db.insert_track(self.artist, self.title, sanitize_lyrics(self.lyrics))
            except LyricError as e:
                self.lyrics = None
                self.db.insert_track_error(self.artist, self.title, e)

        return self.lyrics
       
    def _load_from_file(self):
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
        self.genius = lyricsgenius.Genius(api_secrets.GENIUS_TOKEN, sleep_time=0.5)
        self.genius.remove_section_headers = True

    def get_lyrics(self, artist, title):
        song = self.genius.search_song(title, artist=artist)
        if song and helpers.normalize(song.title) not in helpers.normalize(title):
            raise LyricError(f"MISMATCH ERROR: {song.title}")
        elif not song or len(song.lyrics) <= 1:
            raise LyricError(f"NO LYRICS: {title}")
        return song.lyrics
