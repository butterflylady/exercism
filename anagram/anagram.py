def find_anagrams(word, candidates):
    output = []
    for candidate in candidates:
        if sorted(candidate.lower()) == sorted(word.lower()) and candidate.lower() != word.lower():
            output.append(candidate)
    return output
