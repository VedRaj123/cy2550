#!/usr/bin/env python3
import sys
import random


#file = open('words.txt', 'r')
file = open('/Users/vedrajesh/Desktop/project3/words.txt', 'r')
read = file.readlines()

symb = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]

printword = True


# used for -n and -s as they can be used together
word = [random.choice(read).rstrip('\n'), random.choice(read).rstrip('\n'), random.choice(read).rstrip('\n'), random.choice(read).rstrip('\n')]

for x in range(len(sys.argv)):
    # this represents the -w
    if(sys.argv[x] == "-w" or sys.argv[x] == "-words"):
        count = int(sys.argv[x+1]) - 4
        for x in range(count):
            word.append(random.choice(read).rstrip('\n'))
    # represents -c
    elif(sys.argv[x] == "-c" or sys.argv[x] == "-caps"):
        # if statements to check how many capitalized letters needed
        if(int(sys.argv[x+1]) == 4):
            word[0] = word[0].capitalize()
            word[1] = word[1].capitalize()
            word[2] = word[2].capitalize()
            word[3] = word[3].capitalize()
        if(int(sys.argv[x+1]) == 3):
            a = 0
            b = 0
            c = 0
            while(a == b or a == c or b ==c):
                a = random.randint(0, 3)
                b = random.randint(0, 3)
                c = random.randint(0, 3)
            word[a] = word[a].capitalize()
            word[b] = word[b].capitalize()
            word[c] = word[c].capitalize()
        if(int(sys.argv[x+1]) == 2):
            a = 0
            b = 0
            while(a == b):
                a = random.randint(0, 3)
                b = random.randint(0, 3)
            word[a] = word[a].capitalize()
            word[b] = word[b].capitalize()
        if(int(sys.argv[x+1]) == 1):
            a = random.randint(0, 3)
            word[a] = word[a].capitalize()
        break
    # represents -n
    elif(sys.argv[x] == "-n" or sys.argv[x] == "-numbers"):
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
    elif(sys.argv[x] == "-s" or sys.argv[x] == "-symbols"):
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
    elif(sys.argv[x] == "-h" or sys.argv[x] == "-help"):
        printword = False
        print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS] \n"
        "Generate a secure, memorable password using the XKCD method"
        "optional arguments:"
    "-h, --help            show this help message and exit"
    "-w WORDS, --words WORDS"
   "                       include WORDS words in the password (default=4)"
   " -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words"
                          "(default=0)"
   " -n NUMBERS, --numbers NUMBERS"
                          "insert NUMBERS random numbers in the password"
                          "(default=0)"
   " -s SYMBOLS, --symbols SYMBOLS"
                          "insert SYMBOLS random symbols in the password"
                          "(default=0)")

#puts all the words together at the end
if printword:
    words = ""
    for x in range(len(word)):
        words += word[x]
    print(words)