import re
import nltk
import itertools

nltk.download('words')

def join_and_filter_all_lyrics(lyrics_list):
    all_lyrics = " ".join(lyrics_list) 
    all_lyrics = re.sub(r"[\(\[].*?[\)\]]", "", all_lyrics) # remove everything within parentheses or brackets
    all_lyrics =  re.sub(r"[”“\"!\-;.,?\)\()]", "", all_lyrics) # remove remaining special characters
    return all_lyrics

def lyrics_to_word_list(lyrics, keep_lines=True):
    if keep_lines:
        line_list = re.split(r'(\n)', lyrics)
        word_list = [line.split(' ') for line in line_list] # split by word
        word_list  = list(itertools.chain(*word_list))
    else:
        word_list = lyrics.split()

    word_list = [word.lower() for word in word_list if word not in ["I", "I've", "I'll", "I'm"]]
    return word_list

def only_english_words(word_list):
    words = set(nltk.corpus.words.words())
    english_lyrics = [word for word in word_list if word.lower() in words or not word.isalpha()]
    return english_lyrics

def write_to_file(file_name, text):
    f = open(file_name, "a", encoding="utf-8")
    f.write(f"\n{text}\n")
    f.close()

def normalize(title):
    return (re.sub('[^A-Za-z0-9]+', '', title.lower()))