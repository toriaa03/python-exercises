import time



print("Welcome to the game, Hangman!")
time.sleep(1)
print("Alright, lets play! Start guessing...")
time.sleep(1)
guesses = ''
secret_word = "python"
turns = 10

while turns > 0:
    for letter in secret_word:
        if letter in guesses:
            print (letter),
        else:
            print ("I'm sorry, that letter doesn't appear to be in the word.")
        break


guess = input("Guess a letter:")
guesses = guess