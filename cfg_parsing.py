import nltk
from nltk import CFG

grammar1 = CFG.fromstring("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
PropN -> 'Buster' | 'Chatterer' | 'Joe'
Det -> 'the' | 'a'
N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
Adj -> 'angry' | 'frightened' | 'little' | 'tall'
V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put'
P -> 'on' | 'at'
""")

parser = nltk.RecursiveDescentParser(grammar1)
sentence1 = "the angry bear chased the frightened little squirrel".split()

print(sentence1)

for t in parser.parse(sentence1):
    print(t)
