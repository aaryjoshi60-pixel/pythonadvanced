import random

def hangman():
    wordlist = ["Portugal", "Canada", "Thailand", "India", "France", "Russia", "Laos", "Mexico", "Bahrain", "Ireland", "China", "Italy", "Japan", "Brazil", "Chile", "Iceland", "Kenya"]

    word = random.choice(wordlist).lower()
    #display is the guessed word to keep track of the word guessing by the user
    display  = "_" * len(word)

    maxattempts = 8
    attempts = 0
    guessed = []

    print("Welcome to Ari's Hangman game!")
    print("Word: "+" ".join(display))

    while(attempts<maxattempts and "_" in display):
        guess = input("\n Enter a letter:   "),lower()


        if len(guess)!=1 or not guess.isalpha():
            print("Please enter a single vaild letter")
            continue 

       if guess in guessedletters:
        print("You have already guessed that letter")
        continue 

       guessedletters.append(guess)
    
       if guess in word:
        print("Correct! This letter is in the word!".format(guess))
        

    


        

