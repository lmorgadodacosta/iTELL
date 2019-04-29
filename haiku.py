import random
import wn
import syl

print("The title of your haiku is:",  "the", wn.randomword('a','eng'), wn.randomword('n', 'eng'))

while True:
    line1 = input("Type your haiku here:\n")
    counter1 = syl.noofsyllables(line1)
    if counter1 != 5:
        print("There should be exactly 5 syllables in line 1. I counted " + str(counter1) )
    if counter1 == 5:
        break


#while True:
    #line2 = input()
    #counter2 = syl.noofsyllables(line2)
    #if counter2 != 7:
        #print("There should be exactly 7 syllables in line 2. I counted " + str(counter2))
    #if counter2 == 7:
        #break


rannum = random.randint(1,5)
ranword = wn.randomword('a','eng')

while True:
    if rannum in [1,2,3,4,5]:
        print ("You must use", '"', ranword, '"', "in this second line.")
        line2 = input()
        wordlist = line2.split()
        #swordlist= stripped wordlist
        swordlist = []
        for word in wordlist:
            word = word.lower().strip(".:;?!")
            swordlist.append(word)
            print (swordlist)
        if ranword in swordlist:
            counter2 = syl.noofsyllables(line2)
            if counter2 != 7:
                print("There should be exactly 7 syllables in line 2. I counted " + str(counter2))
            if counter2 == 7:
                break
        else:
             print  ("You must try again.")
    else:
        line2 = input()
        counter2 = syl.noofsyllables(line2)
        if counter2 != 7:
            print("There should be exactly 7 syllables in line 2. I counted " + str(counter2))
        if counter2 == 7:
            break


while True:
    line3 = input()
    counter3 = syl.noofsyllables(line3)
    if counter3 != 5:
        print("There should be exactly 5 syllables in line 3. I counter " + str(counter3))
    if counter3 == 5:
        break

print("Good job! This is your haiku: \n")
print (line1 + "\n" + line2 + "\n" + line3)
