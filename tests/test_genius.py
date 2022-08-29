from .context import gazerbot
from gazerbot import genius
import pytest


def test_get_lyrics():
    artist = "The Beatles"
    song = "Yesterday"
    lyrics = genius.get_lyrics(artist, song)

    assert "All my troubles seemed" in lyrics

def test_get_nonexistent_lyrics():
    artist = "The Beatles"
    song = "Not Yesterday"
    lyrics = genius.get_lyrics(artist, song)

    assert not lyrics
