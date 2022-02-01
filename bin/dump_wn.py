from collections import defaultdict as dd
from nltk.corpus import wordnet as wn
import nltk


def extracthypos(synset, limit=999):
    """Given a synset object, return a set with all synsets 
    underneath it in the PWN structure (including the original)."""
    l = limit-1
    result = []
    result.append(synset)
    if synset.hyponyms() and l > 0:
        for each in synset.hyponyms():
            x = extracthypos(each, l)
            result += x
    return result




exclude_ss = []

exclude_hypos_of = [
    '01326291-n',     # microorganism
    '07992450-n',      # taxonomic group
    '14939445-n'    # fluid (will be mass)
]

for synset in exclude_hypos_of:

    ss_set = extracthypos(wn.of2ss(synset))
    for ss in ss_set:
        exclude_ss.append(ss)

pwn = open('pwn_data.py', 'w+')
pwn.write("from collections import defaultdict as dd\n")
pwn.write("pwn = dd(lambda: dd())\n")

for ss in wn.all_synsets():

    if ss not in exclude_ss:
    
        pos = ss.pos()
        if pos == 's':
            pos = 'a'

        ss.name()

        lem_list = ss.lemma_names('eng')
        pwn.write('''pwn["{}"]["{}"]={}\n'''.format(pos,
                                                    ss.name(),
                                                    str(lem_list)
        ))


        
pwn.close()
