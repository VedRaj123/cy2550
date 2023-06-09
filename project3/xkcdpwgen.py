import sys
import random


file = open('words.txt', 'r')
read = file.readlines()

symb = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]


# used for -n and -s as they can be used together
word = [random.choice(read).rstrip('\n'), random.choice(read).rstrip('\n'), random.choice(read).rstrip('\n')]

for x in range(len(sys.argv)):
    # this represents the -w
    if(sys.argv[x] == "-w"):
        count = int(sys.argv[x+1]) - 3
        for x in range(count):
            word.append(random.choice(read).rstrip('\n'))
    # represents -c
    elif(sys.argv[x] == "-c"):
        # if statements to check how many capitalized letters needed
        if(int(sys.argv[x+1]) == 3):
            word[0] = word[0].capitalize()
            word[1] = word[1].capitalize()
            word[2] = word[2].capitalize()
        if(int(sys.argv[x+1]) == 2):
            a = 0
            b = 0
            while(a == b):
                a = random.randint(0, 2)
                b = random.randint(0, 2)
            word[a] = word[a].capitalize()
            word[b] = word[b].capitalize()
        if(int(sys.argv[x+1]) == 1):
            a = random.randint(0, 2)
            word[a] = word[a].capitalize()
        break
    # represents -n
    elif(sys.argv[x] == "-n"):
        count = int(sys.argv[x+1])
        for x in range(3):
            #randomly chooses how many numbers should be added and what random number
            randomNum = random.randint(0, count)
            if(count - randomNum >= 0):
                count = count - randomNum
            if(count >= 0):
                for y in range(randomNum):
                    word[x] = str(random.randint(0, 9)) + word[x]
        if(count > 0):
            for x in range(count):
                word += str(random.randint(0, 9))
    # represents -s
    elif(sys.argv[x] == "-s"):
        count = int(sys.argv[x+1])
        for x in range(3):
            #randomly chooses how many symbols should be added and what random symbol
            randomNum = random.randint(0, count)
            if(count - randomNum >= 0):
                count = count - randomNum
            if(count >= 0):
                for y in range(randomNum):
                    word[x] += symb[(random.randint(0, 11))]
        if(count > 0):
            for x in range(count):
                word += symb[(random.randint(0, 11))]


#puts all the words together at the end
words = ""
for x in range(len(word)):
    words += word[x]
    
print(words)