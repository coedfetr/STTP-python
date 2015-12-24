def vow(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True

def translate(string):
    results = []
    for word in string.split():
        result = ''
        for char in word:
            if not vow(char):
                result += char + 'o' + char
            else:
                result += char
        results.append(result)
    return ' '.join(results)


print translate("This is Fun")