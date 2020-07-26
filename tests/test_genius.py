from .context import gazerbot
import pytest

def test_get_lyrics():
    assert gazerbot.genius.get_lyrics()

