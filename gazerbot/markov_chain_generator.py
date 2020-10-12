import numpy as np
import random
import re
from collections import defaultdict
from gazerbot import helpers, analyzers

def generate_songs(lyrics_list, song_length, num_to_generate):
  songs = []
  markov_graph = create_graph(lyrics_list)
  for i in range(num_to_generate):
    songs.append(markov_chain_generator(markov_graph, song_length))
  return songs

def markov_chain_generator(markov_graph, num_words):
    song = ' '
    song = ' '.join(_walk_graph(markov_graph, distance=(num_words)))
    return song

def create_graph(lyrics_list):
    all_lyrics = helpers.join_and_filter_all_lyrics(lyrics_list)
    word_list = helpers.lyrics_to_word_list(all_lyrics)

    # Create graph.
    markov_graph = defaultdict(lambda: defaultdict(int))

    last_word = word_list[0].lower()
    for word in word_list[1:]:
        word = word.lower()
        markov_graph[last_word][word] += 1
        last_word = word
    
    return markov_graph

def _walk_graph(graph, distance=5, start_node=None):
  """Returns a list of words from a randomly weighted walk."""
  if distance <= 0:
    return []
  
  # If not given, pick a start node at random.
  if not start_node:
    start_node = random.choice(list(graph.keys()))
  
  weights = np.array(
      list(graph[start_node].values()),
      dtype=np.float64)
  # Normalize word counts to sum to 1.
  weights /= weights.sum()

  # Pick a destination using weighted distribution.
  choices = list(graph[start_node].keys())
  chosen_word = np.random.choice(choices, None, p=weights)
  
  return [chosen_word] + _walk_graph(
      graph, distance=distance-1,
      start_node=chosen_word)
  
