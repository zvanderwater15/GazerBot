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


