import re
from collections import Counter
from typing import List


def count_top_10_words(string: str) -> List[int]:
    """
    Counts top 10 word in given text.
    """
    word_regex = re.compile("[A-Яа-яA-Za-z]+")
    words = {}
    for word in word_regex.findall(string):
        word_lower = word.lower()
        if word not in words:
            words[word_lower] = 0
        words[word_lower] += 1
    return [word for word, frequency in Counter(words).most_common(10)]


def count_sentences(string: str) -> int:
    """
    Counts quantity of sentences in given text.
    """
    sentence_endings = re.compile(".*[.!?].*")
    return len(sentence_endings.findall(string))
