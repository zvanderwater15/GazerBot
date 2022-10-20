from .context import gazerbot
from gazerbot import lyrics as _lyrics
import pytest


def test_get_lyrics():
    artist = "The Beatles"
    song = "Yesterday"
    genius = _lyrics.Genius()
    lyrics = genius.get_lyrics(artist, song)

    assert "All my troubles seemed" in lyrics

def test_get_nonexistent_lyrics():
    artist = "The Beatles"
    song = "not yesterday"
    genius = _lyrics.Genius()
    with pytest.raises(_lyrics.LyricError):
        genius.get_lyrics(artist, song)
