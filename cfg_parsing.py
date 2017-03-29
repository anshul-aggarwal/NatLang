import nltk
from nltk import CFG

grammar1 = CFG.fromstring("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
Det -> 'the' | 'an' | 'a'
N -> 'bear' | 'squirrel' | 'tree'
Adj -> 'angry' | 'frightened' | 'little' | 'short'
V -> 'chased'
P -> 'on' | 'at'
""")

parser = nltk.RecursiveDescentParser(grammar1)
sentence1 = "the angry bear chased the frightened little squirrel on the tree".split()

print(sentence1)

for t in parser.parse(sentence1):
    print(t)
