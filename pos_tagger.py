#Part-of-speech tagger

import nltk
from nltk import word_tokenize

txt = open("0", "r").read()

tokens = word_tokenize(txt)
pos = nltk.pos_tag(tokens)

print(pos)
