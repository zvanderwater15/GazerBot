from gazerbot import spotify, genius, markov_chain_generator, naive_shuffler, analyzers, secrets, helpers
import re
import random 

lyrics_list = []
results_file = "personalmegaplaylist.txt"
markov_lyrics_to_generate = 40
user = 'zoiaran'
playlist = 'All Monthly Playlists 2017-?'
helpers.write_to_file(results_file, playlist)
for track in spotify.get_tracks_from_playlist(user, playlist):
    lyrics = genius.get_lyrics(track["artist"], track["title"])
    if lyrics:
        lyrics_list.append(lyrics)
    
average_word_count = analyzers.average_word_count(lyrics_list)
average_line_count = analyzers.average_num_lines(lyrics_list)
stats = f"STATS:\n AVE WORDS: {average_word_count}\nAVE LINES: {average_line_count}"
helpers.write_to_file(results_file, stats)

helpers.write_to_file(results_file, "MARKOV CHAIN (basically predictive text) GENERATED LYRICS")
markov_songs = markov_chain_generator.generate_songs(lyrics_list, average_word_count + 40, markov_lyrics_to_generate)
for song in markov_songs:
    title = random.choice(song.split()) + random.choice(song.split())
    print(f"\n\n----{title}------")
    helpers.write_to_file(results_file, f"\n\n-----{title}------")
    print(song)
    helpers.write_to_file(results_file, song)

