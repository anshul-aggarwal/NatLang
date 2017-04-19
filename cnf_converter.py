#Convert Context-Free Grammars into Chomsky Normal Form

import nltk
import re
from math import floor

gmr = """
S -> Ax B
Ax -> 'a' Ax 'b' | 'b'
B -> 'c' B | 'c'
"""

rules = gmr.split("\n")
rules = [rule for rule in rules if rule != ""]

nonterminals = re.findall("([A-Z]+[A-Za-z0-9]*)\s->", gmr)

ctr = 0 #Counter for non terminals
rules2 = [] #list of modified rules


#Split OR conditions, and remove terminal-nonterminal combinations
for rule in rules:
    left = re.findall("([A-Z]+[A-Za-z0-9]*)\s->",rule)  #left side of rules
    right = re.findall("->([^\n\t]+)", rule)    #right side of rules
    rt = right[0].split("|")    #Split all OR cases
    extrarules = [] #temporary list to store extra rules
    for r in rt:
        flag = 0
        ter = re.findall("'[a-z]+'",r)      #List of terminals
        nt = re.findall("[A-Z]+[A-Za-z0-9]*",r)     #List of non terminals
        if len(ter) > 0 and len(nt) > 0:
            for tr in ter:
                new_nt = "Y" + str(ctr)     #New non terminal
                ctr = ctr + 1
                nrule = new_nt + " -> " + tr    #New rule for the new non terminal created
                extrarules.append(nrule)
                newr = left[0] + " ->" + r.replace(tr, new_nt)  #modifying original rule
                flag = 1
                rules.append(newr)
                break
        if flag == 1:
            rt.remove(r)
    for r in rt:
        newrule = left[0] + " ->" + r   #recreate the rules from left and right segments
        rules2.append(newrule)
    rules2 = rules2 + extrarules
    

#Modify to include only pairs of non-terminals
for rule in rules2:
    left = re.findall("([A-Z]+[A-Za-z0-9]*)\s->",rule)  #left side of rules
    right = re.findall("->([^\n\t]+)", rule)        #right side of rules
    rt_nt = re.findall("([A-Z]+[A-Za-z0-9]*)\s",right[0])   #List of right non-terminals
    if len(rt_nt) >= 3:
        new_nt = "Y" + str(ctr) #New Non terminal
        ctr = ctr + 1
        nrule = new_nt + " -> " + rt_nt[0] + " " + rt_nt[1]      #New rule for the new non terminal created
        modrule = rule.replace(rt_nt[0] + " " + rt_nt[1], new_nt)   #modifying original rule
        rules2.remove(rule)
        rules2.append(modrule)
        rules2.append(nrule)
        
for rule in rules2:
    print(rule)
