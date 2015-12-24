import re

def correct(string):
    string = re.sub(r'[.]([a-zA-Z])', r'. \1', string)
    string = re.sub(r'( )+', r'\1', string)
    return string

print correct("This   is  very funny  and    cool.Indeed!")