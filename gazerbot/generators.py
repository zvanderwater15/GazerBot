import random
import re

def shuffle_lyrics_naive(lyrics_list, num_lines, num_words):
    all_lyrics = _join_and_filter_all_lyrics(lyrics_list)
    word_list = _lyrics_to_word_list(all_lyrics)
    randomized_lyrics = _new_song_from_word_list(word_list, num_lines, num_words)
    return randomized_lyrics

def shuffle_lyrics_structured(verses, choruses):
    return None

def markov_chain_generator(lyrics_list):
    return None

def _join_and_filter_all_lyrics(lyrics_list):
    all_lyrics = " ".join(lyrics_list) 
    all_lyrics = re.sub(r"[\(\[].*?[\)\]]", "", all_lyrics) # remove everything within parentheses or brackets
    return all_lyrics

def _lyrics_to_word_list(lyrics):
    word_list = lyrics.split() # split by word
    word_list = [word.lower() for word in word_list if word not in ["I", "I've", "I'll", "I'm"]]
    random.shuffle(word_list) # shuffle words randomly 
    return word_list

def _new_song_from_word_list(word_list, num_lines, num_words):
    shortened_word_list = word_list[:num_words]
    for i in range(num_lines):
        shortened_word_list.append("\n") # add new lines to the new song
    random.shuffle(shortened_word_list) # shuffle words randomly
    new_song = ' '.join(shortened_word_list) # put all the words into one song and limit song length
    new_song = re.sub(r"[”“\"!\-;.,?]", "", new_song)
    return new_song

