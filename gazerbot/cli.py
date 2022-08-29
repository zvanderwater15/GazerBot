from gazerbot import spotify, genius, markov_chain_generator, naive_shuffler, analyzers, secrets, helpers
import re
import random 
import click

@click.group()
def generate():
    pass

@generate.command()
@click.option('--user', prompt=True, help='spotify user that owns the playlist')
@click.option('--playlist', prompt=True, help='playlist to grab songs from')
@click.option('--numsongs', prompt=True, default=5, help='number of lyric groups to generate')
@click.option('--fout', prompt=True, default='results.txt', help='Output file to print generate lyrics to')
def lyrics(user, playlist, numsongs, fout):
    lyrics_list = []
    helpers.write_to_file(fout, f"PLAYLIST: \n {playlist}")
    tracks = spotify.get_tracks_from_playlist(user, playlist)
    if not len(tracks):
        print("Playlist not found")
        raise (SystemExit)

    for track in spotify.get_tracks_from_playlist(user, playlist):
        lyrics = genius.get_lyrics(track["artist"], track["title"])
        if lyrics:
            lyrics_list.append(lyrics)
        
    average_word_count = analyzers.average_word_count(lyrics_list)
    average_line_count = analyzers.average_num_lines(lyrics_list)
    stats = f"STATS:\n AVE WORDS: {average_word_count}\nAVE LINES: {average_line_count}"
    helpers.write_to_file(fout, stats)

    helpers.write_to_file(fout, "MARKOV CHAIN (basically predictive text) GENERATED LYRICS")
    markov_songs = markov_chain_generator.generate_songs(lyrics_list, average_word_count + 40, numsongs)
    for song in markov_songs:
        title = random.choice(song.split()) + random.choice(song.split())
        helpers.write_to_file(fout, f"\n\n-----{title}------")
        helpers.write_to_file(fout, song)

