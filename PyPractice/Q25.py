target = 'tiger'
input = raw_input('')

while input != target:
    output = ''
    for pos, char in enumerate(input):
        if char in target:
            if target[pos] == input[pos]:
                output += '[' + char + ']'
            else:
                output += '(' + char + ')'
        else:
            output += char

    print "Clue: " + output
    input = raw_input('')

print "Found!"