from .context import gazerbot
from gazerbot import spotify
import pytest

user = "zoiaran"
invalid_user = "soiethsiuertaeuthyaeiutg"
playlist = "ipod sim"
invalid_playlist = "erseaeinkoiznhdtrr"

def test_get_playlists():
    playlists = spotify.get_user_playlists(user)
    assert playlists
    assert playlists[0]["name"]
    assert playlists[0]["id"]

def test_get_playlists_for_nonexistent_user():
    playlists = spotify.get_user_playlists(invalid_user)
    assert not playlists

def test_get_tracks_from_playlist():
    tracks = spotify.get_tracks_from_playlist(user, playlist)
    assert tracks

def test_get_tracks_from_nonexistent_playlist():
    tracks = spotify.get_tracks_from_playlist(user, invalid_playlist)
    assert not tracks
