# -*- coding: utf-8 -*-

import nltk
nltk.download('punkt')
#essays = u"""text here"""


jabber = open("C:/Users/Scott/Documents/GitHub/PythonTestCode/tarzanoftheapes.txt")

for line in jabber:
    print(line)
    
tokens = nltk.word_tokenize(jabber)
tagged = nltk.pos_tag(tokens)
#nouns = [word for word,pos in tagged \
#	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
#downcased = [x.lower() for x in nouns]
#joined = " ".join(downcased).encode('utf-8')
#into_string = str(nouns)

#output = open("output.txt", "w")
#output.write(joined)
#output.close()

        
jabber.close()

