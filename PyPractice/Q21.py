def numbered_file(filepath):
    file_in = open(filepath)
    file_out = open('Q21_out.txt', 'w')
    
    for line, content in enumerate(file_in):
        file_out.write('%s %s' % (line + 1, content))


numbered_file('Q21.txt')