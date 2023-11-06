from os import system

system('cls')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Step 1 
word_list = ["Dog","Cat","Elephant","Lion","Tiger","Giraffe","Horse","Zebra","Kangaroo","Koala","Panda","Penguin","Dolphin","Whale","Octopus","Snake","Frog","Turtle","Ostrich","Gorilla"]

#TO DO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

live = word_length

display = []
for _ in range(word_length):
    display += "_"


# Asking the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Checking if the letter the user guessed (guess) is one of the leters in the chosen_word.

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
        #If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1. 
        #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word :
        live -=1
        if live == 0 :
            end_of_game = True
            print("You Lose !! ")

        #Join all the elements in the list and turn it into a String.

    print(f"{' '.join(display)}")
    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[live])

    
for letter in chosen_word:
    if guess == letter :
        print(guess,end="")
    else:
        print(" _ ",end="")
