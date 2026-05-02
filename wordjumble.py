import random

wordlist - ["astrounat", "NASA", "orbit", "planet","meteors","earth","comet","star","moon","telescope" , "eclipse", "galaxy","universe"]

def jubleword(word):
    wordlist = list(word) #word into list
    random.shuffle(wordlist) #shuffle the list 
    "".join(wordlist) #combine the word and return it 

def givehint(word):
    hint = word[0].upper()
    return hint 

def playgame():
    score = 0
    rounds = 4

    print("Welcome to Aaryav's Space word Jumble!")

    for i in range(1,round5+1):
        #choose a random word
        word = random.choice(wordlist)
        jword = jumbleword(word)

        print("Round:[]".format(1))
        print("Here is the Scrambled word: {}",.format(jword))