from venv import create
import numpy as np
import random
import re
from collections import defaultdict

from gazerbot import helpers, analyzers

class GeneratedSong:
  def __init__(self, title, lyrics):
    self.title = title
    self.lyrics = lyrics

class MarkovGraph:
  def __init__(self, lyrics_list):
    self.lyrics_list = lyrics_list
    self.create_graph()

  def generate_songs(self, song_length, num_to_generate):
    songs = []
    for i in range(num_to_generate):
      generated_lyrics = self.markov_chain_generator(song_length)
      generated_title = random.choice(generated_lyrics.split()) + random.choice(generated_lyrics.split())
      new_song = GeneratedSong(generated_title, generated_lyrics)
      songs.append(new_song)
    return songs

  def markov_chain_generator(self, num_words):
      chain = ' '
      chain = ' '.join(self._walk(self.graph, distance=(num_words)))
      return chain

  def create_graph(self):
      all_lyrics = helpers.join_and_filter_all_lyrics(self.lyrics_list)
      word_list = helpers.lyrics_to_word_list(all_lyrics)

      # Create graph.
      markov_graph = defaultdict(lambda: defaultdict(int))

      last_word = word_list[0].lower()
      for word in word_list[1:]:
          word = word.lower()
          markov_graph[last_word][word] += 1
          last_word = word

      self.graph = markov_graph
      return markov_graph

  def _walk(self, graph, distance=5, start_node=None):
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
    if len(choices) == 0:
      # if no words follow this word in the data, choose the next word at random
      chosen_word = random.choice(list(graph.keys()))
    else:
      chosen_word = np.random.choice(choices, None, p=weights)
    
    return [chosen_word] + self._walk(
        graph, distance=distance-1,
        start_node=chosen_word)





  
