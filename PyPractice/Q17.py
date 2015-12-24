def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True

def make_ing_form(verb):
    if verb.endswith('ie'):
        return verb[:-2] + 'ying'

    elif verb.endswith('e') and (verb[-2].endswith('e') or len(verb) == 2):
        return verb + 'ing'

    elif verb.endswith('e'):
        return verb[:-1] + 'ing'

    elif not is_vowel(verb[-1]) and is_vowel(verb[-2]) and not is_vowel(verb[-3]):
        return verb + verb[-1] + 'ing'
        
    else:
        return verb + 'ing'



print make_ing_form('be')
print make_ing_form('lie')
print make_ing_form('see')
print make_ing_form('move')
print make_ing_form('hug')