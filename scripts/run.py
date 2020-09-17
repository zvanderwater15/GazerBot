from gazerbot import spotify, genius, markov_chain_generator, naive_shuffler, analyzers, secrets, helpers
import re

lyrics_list = []
results_file = "results.txt"
num_lyrics_to_generate = 5
user = 'zoiaran'
playlist = 'Calmest'
helpers.write_to_file(results_file, playlist)
for track in spotify.get_tracks_from_playlist(user, playlist):
    lyrics = genius.get_lyrics(track["artist"], track["title"])
    if lyrics:
        lyrics_list.append(lyrics)
    
average_word_count = analyzers.average_word_count(lyrics_list)
average_line_count = analyzers.average_num_lines(lyrics_list)
stats = f"STATS:\n AVE WORDS: {average_word_count}\nAVE LINES: {average_line_count}"
helpers.write_to_file(results_file, stats)

helpers.write_to_file(results_file, "RANDOMIZED LYRICS")
for i in range(1, num_lyrics_to_generate + 1):
    generated_lyrics = naive_shuffler.shuffle_lyrics_naive(lyrics_list, average_line_count, average_word_count)
    print(f"\n\n-----SONG {i}------")
    print(generated_lyrics)
    helpers.write_to_file(results_file, generated_lyrics)

helpers.write_to_file(results_file, "MARKOV CHAIN LYRICS")
for i in range(1, num_lyrics_to_generate + 1):
    generated_lyrics = markov_chain_generator.markov_chain_generator(lyrics_list, average_line_count)
    print(f"\n\n-----SONG {i}------")
    print(generated_lyrics)
    helpers.write_to_file(results_file, generated_lyrics)

