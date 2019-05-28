from nltk.corpus import cmudict
cmu_syl = cmudict.dict()

exception = {"am":1, "giant":2, "latecomer":3, "latecomers":3, "penelope":4, "table":2,
"onomatopoeia":6}

allwords = set(["late", "comer", "come", "coming", "cat", "ice", "cream"])

#todo: "The chicken explodes" is counted as 6 syllables, fix it
def syllables(word):
    """
    This function returns the number of syllables in a string. It first 
    checks whether it is a compound, if it is, it calls this function 
    recursively to count the number of syllable of each compound, else, 
    it counts syllables normally. I am also stripping the punctuation 
    and making every letter into lowercase;
    """
    word = word.lower().strip(".:;?!").replace("-", "")


    compoundsyllables = compound(word)
    if compoundsyllables:
        return compoundsyllables

    else:
        count = 0
        vowels = 'aeiouy'
        if word[0] in vowels:
            count +=1
        for index in range(1,len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count +=1
        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count+=1
        if word.endswith('cre'):
            count+=1
        if count == 0:
            count +=1
        return count



def compound(word):
    """ 
    This function returns the number of syllable of a word if it is a
    compound, if not, it returns false, only on the first split
    from the left;
    """
    l=len(word)
    for index in range(0, l):
        if word[:index] in allwords:
            if word[index:] in allwords:
                return (syllables(word[:index]) + syllables(word[index:]))
            elif compound(word[index:]):
                return (syllables(word[:index]) + compound(word[index:]))

    return False

def num_of_syllables(line):
    wordlist = line.split()
    counter = 0
    for word in wordlist:
        counter += nsyl(word)
        # if word in exception:
        #     counter = counter + exception[word]
        # #elif word is a compound then return number of syllable compound
        # else:
        #     counter = counter + syllables(word)
    return counter


def nsyl(word):
    """
    This function computes the nuber of syllables in a word by first 
    trying check if the CMU dictionary has that info. If not, it uses 
    a rule-based system that is not yet completely correct but it's 
    getting there.  When the CMU dictionary provides more than one 
    reading, we are defaulting to the max number of syllables, since 
    the other  values are based on 'fast reading' pronunciations of 
    that same word.
    """
    if word in exception.keys():
        return exception[word]
    else:
        try:
            return max([len(list(y for y in x if y[-1].isdigit())) for x in cmu_syl[word.lower()]]) # returning the max value 
        except KeyError:        
            return syllables(word)
