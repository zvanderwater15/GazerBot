import numpy as np
from collections import Counter

def average_word_count(lyrics_list):
    def word_count(lyrics):
        return len(lyrics.split())
    ave = sum([word_count(lyrics) for lyrics in lyrics_list])/(len(lyrics_list))
    return round(ave)


def average_num_lines(lyrics_list):
    def line_count(lyrics):
        return len(lyrics.split("\n"))
    ave = sum([line_count(lyrics) for lyrics in lyrics_list])/(len(lyrics_list))
    return round(ave)


def analyze_structure(lyrics):
    return {"verses": [], "choruses":[]}


def line_length_probability(lyrics):
    lines = lyrics.split('\n')
    lengths = [len(line.split(" ")) for line in lines if len(line.split(" ")) > 1]
    freq = Counter(lengths)
    lengths_set = list(freq.keys())
    weights = np.array(list(freq.values()),dtype=np.float64)
    weights /= weights.sum()   # Normalize weights to sum to 1.
    return lengths_set, weights
