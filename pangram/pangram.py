import string

def is_pangram(sentence):
    """
    Returns True if a sentence is a pangram (a sentence using every letter of the alphabet at least once).
    """
    sentence_set = set(sentence.lower())
    ascii_set = set(string.ascii_lowercase)
    return ascii_set.issubset(sentence_set)
