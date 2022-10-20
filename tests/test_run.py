from .context import gazerbot
from gazerbot import cli

import os
import pytest


def test_full_run():
    num_songs = 5
    results = cli.run("ZoiAran", "September 2022", num_songs)
    assert results["average_lines"] > 0
    assert results["average_words"] > 0
    assert len(results["songs"]) == num_songs
    for song in results["songs"]:
        assert song.title
        assert song.lyrics