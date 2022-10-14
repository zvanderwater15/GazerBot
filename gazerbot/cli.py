from . import lyrics as _lyrics, markov, spotify, analyzers, helpers
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
    output = run(user, playlist, numsongs)
    playlist_info = {"title": playlist, "Average Words": output["average_words"], "Average Lines": output["average_lines"]}
    output_to_file(fout, playlist_info, output["songs"])


def output_to_file(fout, playlist_info, songs):
    print(playlist_info)
    for key in playlist_info:
        helpers.write_to_file(fout, f"{key}: \n {playlist_info[key]}")

    helpers.write_to_file(fout, "MARKOV CHAIN (basically predictive text) GENERATED LYRICS")
    for song in songs:
        helpers.write_to_file(fout, f"\n\n-----{song.title}------")
        helpers.write_to_file(fout, song.lyrics)


def run(user, playlist, numsongs):
    lyrics_list = []
    tracks = spotify.get_tracks_from_playlist(user, playlist)
    if not len(tracks):
        print("Playlist not found")
        raise 
    genius = _lyrics.Genius()
    for track in tracks:
        song = _lyrics.Song(track["artist"], track["title"])
        lyrics = song.get_lyrics(genius)
        if lyrics:
            lyrics_list.append(lyrics)

    average_word_count = analyzers.average_word_count(lyrics_list)
    average_line_count = analyzers.average_num_lines(lyrics_list)
    markov_graph = markov.MarkovGraph(lyrics_list)
    markov_songs = markov_graph.generate_songs(average_word_count + 40, numsongs)
    return {"average_words": average_word_count, "average_lines": average_line_count, "songs": markov_songs}
