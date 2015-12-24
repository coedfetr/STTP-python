import re


def make_3sg_form(verb):
    es = ('o', 'ch', 's', 'sh', 'x', 'z')
    if verb.endswith('y'):
        return re.sub('y$', 'ies', verb)
    elif verb.endswith(es):
        return verb + 'es'
    else:
        return verb + 's'


print make_3sg_form('try')
print make_3sg_form('brush')
print make_3sg_form('run')
print make_3sg_form('fix')