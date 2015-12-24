import re

def char_freq_table(filepath):
    file = open(filepath)
    chars = file.read().lower().replace(" ", "").replace("\n", "")
    freqs = {key: 0 for key in chars}
    for char in chars:
        freqs[char] += 1
    for word in freqs:
        print "%s: %s" % (word, freqs[word])


char_freq_table('Q20.txt')