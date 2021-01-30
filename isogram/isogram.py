def is_isogram(string):
    s = string.replace(" ", "")
    s = s.replace("-", "")
    return len(set(s.lower())) == len(s)
