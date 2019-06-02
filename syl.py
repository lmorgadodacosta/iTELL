exception = {"giant":2,
"latecomer":3,
"latecomers":3,
"penelope":4,
"table":2,
"I'll":1,
"you'll":1,
"he'll":1,
"you'll":1,
"she'll":1,
"they'll":1,
"who'll":1,
"I'm":1,
"you're":1,
"we're":1,
"they're":1,
"he's":1,
"she's":1,
"What's":1,
"where's":1,
"who's":1,
"when's":1,
"that's":1,
"there's":1,
"there're":1,
"who're":1,
"where're":1,
"can't":1,
"couldn't":2,
"mustn't":2,
"doesn't":2,
"wouldn't":2,
"shouldn't":2,
"shan't":1,
"needn't":2,
"oughtn't":2,
"won't":1,
"don't":1,
"wasn't":2,
"haven't":2,
"hasn't":2,
"aren't":1,
"were't":1,
"ain't":1,
"I've":1,
"You've":1,
"should've":2,
"would've":2,
"could've":2,
"they've":1,
"must've":2,
"I'd":1,
"you'd":1,
"he'd":1,
"she'd":1,
"we'd":1,
"they'd":1,
"where'd":1,
"y'all":1,
"McDonald":3,
"onomatopoeia":6}

allwords = set(["late", "comer", "come", "coming", "cat", "ice", "cream"])

#todo: "The chicken explodes" is counted as 6 syllables, fix it
def syllables(word):
    """
    This function returns the number of syllables in a string. It first checks
    whether it is a compound, if it is, it calls this function recursively to
    count the number of syllable of each compound, else, it counts syllables
    normally. I am also stripping the punctuation and making every letter
    into lowercase;
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
        if word in exception:
            counter = counter + exception[word]
        #elif word is a compound then return number of syllable compound
        else:
            counter = counter + syllables(word)
    return counter
