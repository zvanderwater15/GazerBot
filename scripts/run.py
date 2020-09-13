from gazerbot import spotify, genius, generators, analyzers
import re

lyrics_list = []
num_lyrics_to_generate = 10
for track in spotify.get_tracks_from_playlist("zoiaran", "my idiot dna"):
    if track["artist"] != "Lacing":
        lyrics = genius.get_lyrics(track["artist"], track["title"])
        print(lyrics)
        if lyrics:
            lyrics_list.append(lyrics)
    
average_word_count = analyzers.average_word_count(lyrics_list)
average_line_count = analyzers.average_num_lines(lyrics_list)

for i in range(1, num_lyrics_to_generate + 1):
    generated_lyrics = generators.shuffle_lyrics_naive(lyrics_list, average_line_count, average_word_count)
    print(f"\n\n-----SONG {i}------")
    print(generated_lyrics)
