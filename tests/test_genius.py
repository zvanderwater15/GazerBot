from .context import gazerbot
from gazerbot import genius
import pytest

def test_get_lyrics():
    assert genius.get_lyrics()
