f=open('data/bsls', 'r')
#print(type(f))
#print(type("cat"))
a=open('new.txt','w')
for line in f:

    #print(line.split())
    wordlist=line.split()

    for word in wordlist:
        print(word)
        a.write(str(word)+ "\n")

a.close ()
f.close ()

### VERSION 2 (WORSE)

f=open('data/bsls', 'r')
a=open('new.txt','w')
string_to_write_to_file = ""
for line in f:

    #print(line.split())
    wordlist=line.split()

    for word in wordlist:
        print(word)
        string_to_write_to_file = string_to_write_to_file + str(word)+ "\n"
        #a.write(str(word)+ "\n")
a.write(string_to_write_to_file)
a.close ()
f.close ()
