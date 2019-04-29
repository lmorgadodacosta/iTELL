import random

characters = ["Batman",  "Superman", "Superwoman", "Spiderman", "a nun", "the Pope", "Ms. Frizzle", "Obama", "Trump",
            "a yoga instructor"]

contexts = ["at a hospital", "at McDonald", "on a plane", "at the swimming pool", "at home", "at a hawker center",
            "on the moon", "while grabbing on the wing of a plane flying to LA"]

def dialogue (numberoflines):
    rannum1 = random.randint(0, len (characters)-1)
    rannum2 = random.randint(0, len (characters)-1)
    rannum3 = random.randint(0, len (contexts)-1)

    while rannum1 == rannum2:
        rannum2 = random.randint(0, len (characters)-1)


    context = contexts [rannum3]
    characterA = characters [rannum1]
    characterB = characters [rannum2]

    print (characterA + " and " + characterB + " are having a conversation " + context + ":\n")
    linelistA=[]
    linelistB=[]

    for index in range(1, int(numberoflines)+1):
        line=input (characterA + ":")
        linelistA.append (line)
        line=input (characterB + ":")
        linelistB.append (line)

    return characterA, characterB, linelistA, linelistB


numberoflines = input ("How many lines does each character have: ")
A, B, charA, charB = dialogue(numberoflines)
#print (charA, charB)


for index in range(1, int(numberoflines)+1):
    print (A + ": " + charA [index-1])
    print (B + ": " + charB [index-1])
