def is_semordnilap(filepath):
    file = open(filepath)
    words = file.read().split()
    results = []
    for word1 in words:
        for word2 in words:
            if word1 == word2[::-1]:
                results.append(word1)
    return results


print is_semordnilap('Q19.txt')