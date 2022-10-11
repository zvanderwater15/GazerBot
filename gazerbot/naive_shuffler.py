import numpy as np
import random
import re
from gazerbot import helpers

def shuffle_lyrics_naive(lyrics_list, num_lines, num_words):
    all_lyrics = helpers.join_and_filter_all_lyrics(lyrics_list)
    word_list = helpers.lyrics_to_word_list(all_lyrics, keep_lines=False)
    english_word_list = helpers.only_english_words(word_list)
    random.shuffle(english_word_list) # shuffle words randomly 
    randomized_lyrics = _new_song_from_word_list(english_word_list, num_lines, num_words)
    return randomized_lyrics

def _new_song_from_word_list(word_list, num_lines, num_words):
    shortened_word_list = word_list[:num_words]
    for i in range(num_lines):
        shortened_word_list.append("\n") # add new lines to the new song
    random.shuffle(shortened_word_list) # shuffle words randomly
    new_song = ' '.join(shortened_word_list) # put all the words into one song and limit song length
    new_song = re.sub(r"[”“\"!\-;.,?]", "", new_song)
    return new_song

