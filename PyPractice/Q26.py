import sys, re 

def find_position(line):
    
    if re.search(r"[.?!]+", line):
        pun = re.search(r"[.?!]+", line).group()
        pos = line.find(pun)
        pos = pos+len(pun)-1
    else:
        pos = -1
    return pos


def sentence_splitter(filename):

    f = open(filename, "r")

    for line in f:
        line = line.strip()
        while line:
            pos  =  find_position(line)
            if pos != -1:
                line2 = line[ : pos+1].split(" ")
                length = len(line2)
                last_word = line2[length -1]
        
	        try:
                    if re.search(r"[A-Z]+.*", last_word) or  line[pos+1] != " " or line[pos+2].islower() :
	                print line[:pos+1],
	                line = line[pos+1:]


                else:
                print line[ : pos+1]
                    line = line[pos+1 :]
        
                except :
                    print line 
                    line = ""
            else :
                print line
                line = ""
    
    f.close() 
    print        
    return " bye bye"

    
if __name__=="__main__": 
    #print len(sys.argv)
    if len(sys.argv) < 2:
        print 
        print " Please try it as python sentence_splitter.py \"filename\""
        print 
        sys.exit(1)
    else: 
        print sentence_splitter(sys.argv[1])
    