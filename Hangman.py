import random

# List of English words
words = ["apple", "banana", "cat", "dog", "horse"]
# Initialize the game
secret_word = random.choice(words)
b =[]
print("your word is",secret_word)
guessed_letters = []
guesses_remaining = 6
warnings_remaining = 3

# Play the game
while guesses_remaining > 0:
    # Display the current state of the game
    print("Guesses remaining:", guesses_remaining)
    print("Warnings remaining:", warnings_remaining)
    guess=input("enter your guess ")
    print("Letters not guessed",end="")
    h= len(secret_word)
    for i in range(len(secret_word)):
        b.append("-")
        if guess in secret_word[i]:
            b[i]=guess
           
    print(b)
  
   # print("current guessed"," ".join(b))

    # Get the player's guess
    #guess = input("Enter your guess: ")
    # Check the guess
    if not guess.isalpha():
        # The guess is not a letter
        if warnings_remaining > 0:
            warnings_remaining -= 1
            print("That's not a letter. You have {} warnings remaining.".format(warnings_remaining))
        else:
            guesses_remaining -= 1
            print("That's not a letter. You lose a guess.")
        continue

    if guess in guessed_letters:
        # The guess has already been used
        if warnings_remaining > 0:
            warnings_remaining -= 1
            print("You've already guessed that letter. You have {} warnings remaining.".format(warnings_remaining))
        else:
            guesses_remaining -= 1
            print("You've already guessed that letter. You lose a guess.")
        continue

    # The guess is new
    guessed_letters.append(guess)

    # Check if the guess is in the secret word
    if guess in secret_word:
        # The guess is correct
        """
            for i, letter in enumerate( secret_word):
                if letter == guess:
                    guessed_letters[i] = letter"""

        # Check if the player has won
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You won the game!")
            break
    else:
        # The guess is incorrect
        guesses_remaining -= 1
        print("The letter {} is not in the secret word.".format(guess))

# Game over
if guesses_remaining == 0:
    print("You lost the game. The secret word was {}".format(secret_word))

# Calculate the player's score
score = guesses_remaining * len(set(secret_word))
print("Your score is:", score)
