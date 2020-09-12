from gazerbot import spotify, genius, generators
import re

lyrics_list = []
for track in spotify.get_tracks_from_playlist("zoiaran", "Emu"):
    lyrics = genius.get_lyrics(track["artist"], track["title"])
    print(lyrics)
    lyrics_list.append(lyrics)
generated_lyrics = generators.shuffle_lyrics_naive(lyrics_list)
print(generated_lyrics)
average_length = sum([len(lyrics.split()) for lyrics in lyrics_list])/(len(lyrics_list))
print("average word count:", average_length)
