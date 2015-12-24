def char_freq(string):
    freq = {key: 0 for key in string}
    for i in string:
        freq[i] += 1
    return freq



print char_freq("abbabcbdbabdbdbabababcbcbab")