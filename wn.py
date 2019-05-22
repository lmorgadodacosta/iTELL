import random
import nltk
from nltk.corpus import wordnet as wn
import pwn_data
import game_data

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


def randomword(pos, lang):
    """ This function returns a word of a given part of speech in a given
    language based on wordnet."""

    ssl = list(wn.all_synsets(pos))
    lengthoflist = len(ssl)
    rannum = random.randint(0,lengthoflist-1)
    ranss = ssl[rannum] #random synset object
    ss_def = ranss.definition() # definition
    leml = ranss.lemma_names(lang) # lemma list
    lemllen = len(leml) #number of lemmas inside the lemma list
    ranlemnum = random.randint(0,lemllen-1)# random position in the lemma list
    leml[ranlemnum] = leml[ranlemnum].replace("_", " ")
    return (leml[ranlemnum], ss_def)


def x_rand_nouns(x):
    """
    This function returns two random nouns from wordnet.
    It assumes PWN's size for nouns = 82114
    """
    rand_ints = []
    for i in range(0,x):
        rand_ints.append(random.randint(0,82114))
    max_rand = max(rand_ints)
    
    results = []
    for i, ss in enumerate(wn.all_synsets('n')):

        if i > max_rand:
            break

        elif i in rand_ints:
            
            ss_def = ss.definition()
            ss_lemma = random.choice(ss.lemma_names('eng'))
            ss_lemma = ss_lemma.replace("_", " ")

            results.append((ss_lemma,ss_def))
        else:
            continue
        
    return results


def check_lemma(lemma):
    result = True

    exclude_lemmas = ['genus', ' bacteria', ' cell', ' organelle',
                      'pleural']
    for s in exclude_lemmas:
        if s in lemma:
            result = False

    if lemma[0].isupper():
        result = False
        
    return result



def x_rand_pos(x,pos):
    """
    This function returns X random words with a specified POS from 
    the PWN's dump.
    """
    results = []

    while len(results) < x:

        if pos == 'n':
            rand = random.random()
            if rand < 0.25: # mass from list
                article = ''
                all_no_article = game_data.freq_mass_noms + game_data.mass_noms + game_data.characters
                noun = random.choice(all_no_article)
                definition = ''

                if check_lemma(noun):
                    results.append((noun, definition, article))

                
            elif rand < 0.5: # countable from list
                all_with_article = game_data.occupations + game_data.freq_countable_noms
                noun = random.choice(all_with_article)
                definition = ''

                if noun.lower().startswith(('a','e','i','o','u')):
                    article = 'an'
                else:
                    article ='a'

                if check_lemma(noun):
                    results.append((noun, definition, article))

            else: # wordnet random

                pos_dict = pwn_data.pwn[pos]
                ss_name = random.choice(list(pos_dict.keys()))
                ss = wn.synset(ss_name)
                ss_def = ss.definition()
                noun = random.choice(ss.lemma_names('eng'))
                noun = noun.replace("_", " ")
        
                if noun.lower().startswith(('a','e','i','o','u')):
                    article = 'an'
                else:
                    article ='a'

                if check_lemma(noun):
                    results.append((noun, ss_def, article))
        

        else: # if it's not a noun

            article = ''
            pos_dict = pwn_data.pwn[pos]

            ss_name = random.choice(list(pos_dict.keys()))

            ss = wn.synset(ss_name)
            ss_def = ss.definition()
            ss_lemma = random.choice(ss.lemma_names('eng'))
            ss_lemma = ss_lemma.replace("_", " ")
            if pos == 'v':
                ss_lemma = "to " + ss_lemma

            if check_lemma(noun):
                results.append((ss_lemma, ss_def, article))
            
    return results




# def random_countable_noun(lang):
#     """ This function returns a countable noun based on wordnet."""

#     physical_entity = wn._synset_from_pos_and_offset('n',1930)
#     ssl = extracthypos(physical_entity)
#     lengthoflist = len(ssl)
#     rannum = random.randint(0,lengthoflist-1)
    
#     ranss = ssl[rannum] #random synset object
#     ss_def = ranss.definition() # definition
#     # ss_hype = ranss.hypernyms()[0]  # assuming at least 1 hypernym
#     # hype_lem = ss_hype.lemma_names(lang)[0].replace('_',' ')
    
#     leml = ranss.lemma_names(lang) # lemma list
#     lemllen = len(leml) #number of lemmas inside the lemma list
#     ranlemnum = random.randint(0,lemllen-1)# random position in the lemma list
#     leml[ranlemnum] = leml[ranlemnum].replace("_", " ")
#     return (leml[ranlemnum], ss_def)
    


# wordlist = ['alarm clock', 'backpack',  'pillow',  'bedspread',  'blanket',
#             'bookcase',  'book',  'broom',  'brush',  'bucket',  'calendar',
#             'candle',  'carpet',  'chair',  'clock',  'coffee table',  'comb',
#             'computer',  'laptop',  'PS4',  'couch',  'dish towel',  'dishwasher',
#             'door stop',  'drill',  'dryer',  'extension cord',  'fan',
#             'file cabinet',  'fire extinguisher',  'flashlight',  'flower',
#             'fork',  'video game',  'boardgame',  'hammer',  'heater',  'houseplant',
#             'iPhone',  'ironing board',  'piece of jewelry',  'pocket knive',  'lamp',
#             'light bulb',  'light switch',  'fridge magnet',  'microwave',  'mop',
#             'coffee mug',  'piano',  'guitar',  'violin',  'flute',  'dirty napkin',
#             'napkin',  'oven',  'family painting',  'frying pan',  'pair of trousers',
#             'piece of white paper',  'pen',  'pencil',  'photograph',  'pillow',  'pitcher',
#             'plastic plates',  'radiator',  'old radio',  'refrigerator',  'rug',  'saucer',
#             'saw',  'pair of scissors',  'screw driver',  'smoke detector',
#             'pair of sneakers',  'pair of socks',  'spoon',  'suitcase',  'tablecloth',
#             'dinning table',  'box of tissue paper',  'toaster',  'roll of toilet paper',
#             'toothbrush',  'tube of toothpaste',  'towel',  'TV',  'vacuum cleaner',
#             'vase',  'washing machine'];


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
