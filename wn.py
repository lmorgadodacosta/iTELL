import random
import nltk
from nltk.corpus import wordnet as wn



def randomword(pos, lang):
    """ This function returns a word of a given part of speech in a given
    language based on wordnet."""

    #ssl=synsetlist

    ssl = list(wn.all_synsets(pos))
    lengthoflist = len(ssl)
    rannum = random.randint(0,lengthoflist-1)
    ranss = ssl[rannum] #random synset object
    leml = ranss.lemma_names(lang) # lemma list
    lemllen = len(leml) #number of lemmas inside the lemma list
    ranlemnum = random.randint(0,lemllen-1)# random position in the lemma list
    leml[ranlemnum] = leml[ranlemnum].replace("_", " ")
    return leml[ranlemnum]

#this is to print a title of the pattern "the adjective noun"
#print ('the', randomword('a','eng'), randomword('n', 'eng'))

#this is to print a title of the pattern "just verb adverb"
#print ('just', randomword('v', 'eng'), randomword('r', 'eng'))

# print (n)  #TEST
# print (lengthoflist)  #TEST
# print (rannum)  #TEST

#def print_wn_tab(lang):
    #for ss in list(wn.all_synsets()):
        #englemmas = '; '.join(ss.lemma_names('eng'))
        #anglemmas = '; '.join(ss.lemma_names(lang))
        #definition = ss.definition()
        #examples = '; '.join(ss.examples())
        #print(str(ss.name())+ '\t' + str(ss.offset()) + '\t' + englemmas + '\t' + langlemmas + '\t' + definition + '\t' + examples)


#print(print_wn_tab('cmn'))
