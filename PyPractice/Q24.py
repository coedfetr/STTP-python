import random
import itertools

words = ['red', 'black', 'brown', 'green']
word, anagram = random.sample(words, 1)[0], ''

perms = itertools.permutations(word)
for perm in perms:
    if ''.join(perm) != word:
        anagram = ''.join(perm)
        break

print "Colour word anagram: %s" % anagram
input = raw_input("Guess the colour word!\n")

while input != word:
    input = raw_input("Oops, guess the colour word again!\n")

print "Correct!"