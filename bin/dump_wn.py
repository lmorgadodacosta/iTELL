from collections import defaultdict as dd
from nltk.corpus import wordnet as wn
import nltk

exclude = []


pwn = open('pwn_data.py', 'w+')
pwn.write("from collections import defaultdict as dd\n")
pwn.write("pwn = dd(lambda: dd())\n")

for ss in wn.all_synsets():

    pos = ss.pos()
    if pos == 's':
        pos = 'a'
    
    ss.name()

    
    lem_list = ss.lemma_names('eng')
    if ss.name() not in exclude:
        pwn.write('''pwn["{}"]["{}"]={}\n'''.format(pos,
                                                      ss.name(),
                                                      str(lem_list)
                                                      ))

pwn.close()
