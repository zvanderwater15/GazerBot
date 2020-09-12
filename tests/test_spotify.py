from .context import gazerbot
from gazerbot import spotify
import pytest

def test_get_playlists():
    user = "zoiaran"
    playlists = spotify.get_user_playlists(user)
    assert playlists
    print(playlists)
