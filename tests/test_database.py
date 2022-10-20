from .context import gazerbot
from gazerbot import database

import os
import pytest

@pytest.fixture
def db_connection():
    test_db = "test.db"
    file = os.path.expandvars(rf'%APPDATA%/Gazerbot/cache/{test_db}')
    db = database.LyricDatabase(name=test_db)
    connection = db.connect()
    assert os.path.exists(file)
    yield connection
    db.close()
    os.remove(file) # get rid of test database for the next tests

def test_insert_track(db_connection):
    track_artist = "Bright Eyes"
    track_title = "Something Vague"
    track_lyrics = "something vague we're not seeing"
    inserted = db_connection.insert_track(track_artist, track_title, track_lyrics)
    tracks = db_connection.get_all_tracks()
    track = db_connection.get_track(track_artist, track_title)
    assert track["content"] == track_lyrics
    assert track["error"] == None

def test_insert_error(db_connection):
    track_artist = "Bright Eyes"
    track_title = "Nothing Vague"
    track_error = "not found"
    db_connection.insert_track_error(track_artist, track_title, track_error)
    track = db_connection.get_track(track_artist, track_title)
    assert track["content"] == None
    assert track["error"] == track_error



