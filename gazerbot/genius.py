import lyricsgenius
from gazerbot import secrets

def get_lyrics(artist, song):
    genius = lyricsgenius.Genius(secrets.GENIUS_TOKEN)
    song = genius.search_song(song, artist)
    return song.lyrics
