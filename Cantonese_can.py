f=open('data/HKU_all', 'r')
g=open('data/Tatoeba.en-yue.yue', 'r')
a=open('can.txt','w')
characterA='阿'
characterB= '呀'
counter=0
for line in f:
    wordlist=line.split()
    for word in wordlist:
        if word==characterA or word==characterB:
            a.write(str(line)+ "\n")
            counter=counter+1


for line in g:
    wordlist=list(line)
    for word in wordlist:
        if word==characterA or word==characterB:
            a.write(str(line)+ "\n")
            counter+=1


a.close ()
f.close ()
g.close ()

print ("Everything goes well!" + "\n" + str(counter))
