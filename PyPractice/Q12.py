import string

def is_pangram(candidate):
    letters = set(string.ascii_lowercase)
    candidate = set(candidate.replace(" ", "").lower())
    return letters == candidate or False


print is_pangram("The quick brown fox jumps over the lazy dog")
