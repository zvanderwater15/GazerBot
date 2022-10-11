from .context import gazerbot
from gazerbot import lyrics as _lyrics
import pytest


def test_get_lyrics():
    artist = "The Beatles"
    song = "Yesterday"
    genius = _lyrics.Genius()
    track = _lyrics.Song(artist, song)
    lyrics = track.get_lyrics(genius)

    assert "all my troubles seemed" in lyrics

def test_get_nonexistent_lyrics():
    artist = "The Beatles"
    song = "not yesterday"
    genius = _lyrics.Genius()
    track = _lyrics.Song(artist, song)
    lyrics = track.get_lyrics(genius)

    assert not lyrics
