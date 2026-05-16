import random

wordlist = ["astrounat", "nasa", "orbit", "planet","meteors","earth","comet","star","moon","telescope" , "eclipse", "galaxy","universe"]

def jubleword(word):
    wordlist = list(word) #word into list
    random.shuffle(wordlist) #shuffle the list 
    return "".join(wordlist) #combine the word and return it 

def givehint(word):
    hint = word[0].upper()
    return hint 

def playgame():
    score = 0
    rounds = 4
    hintlimit = 2
    hints = 0

    print("Welcome to Aaryav's Space word Jumble!")

    for i in range(1, rounds + 1):
        #choose a random word
        word = random.choice(wordlist)
        jword = jubleword(word)

        print("Round: {}".format(i))
        print("Here is the Scrambled word: {}".format(jword))

        choice = input("Do you want a hint? ").lower()
        if choice == 'yes':
            if hints < hintlimit: 
                hint = givehint(word)
                print("Heres your hint: {}".format(hint))
                hints+=1
            else:
                print("Sorry! No more hints are able to be used.")

        guess = input("What is the word? ")
        if guess.lower() == word.lower():
            print("Good job!")
            score = score + 1
        else:
            print("Bad job, the correct word was: {}".format(word))
    
    print("Your final score is: {}/{}".format(score, rounds))

playgame()
            