import random

def shuffle_lyrics_naive(lyrics_list):
    all_lyrics = " ".join(lyrics_list)
    word_list = list(all_lyrics)
    random.shuffle(word_list)
    new_song = ''.join(word_list)
    return new_song