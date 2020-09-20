import numpy as np
import random
import re
from collections import defaultdict
from gazerbot import helpers, analyzers

def markov_chain_generator(lyrics_list, num_words):
    song = ""
    all_lyrics = helpers.join_and_filter_all_lyrics(lyrics_list)
    word_list = helpers.lyrics_to_word_list(all_lyrics)
    word_list = helpers.only_english_words(word_list)
    # Create graph.
    #TODO create separate graph for each song then combine them
    markov_graph = defaultdict(lambda: defaultdict(int))

    last_word = word_list[0].lower()
    for word in word_list[1:]:
        word = word.lower()
        markov_graph[last_word][word] += 1
        last_word = word

    song = ' '.join(_walk_graph(markov_graph, distance=(num_words+40)))

    return song

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
  
