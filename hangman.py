import random
print("==================================")
print("HANGMAN GAME")
print("==================================")
words = ["ROBOTICS", "MECHATRONICS", "ENGINEERING", "SUCCESS" , "GREATNESS",]

secret_word = random.choice(words)

hidden_word = ["_"]*len(secret_word)

wrong_guesses = 0

guessed_letters = []

print("Guess the hidden word one letter at a time.")
print("You have 6 wrong guesses.")

print("word: ", " ".join(hidden_word))
print("wrong guesses: ", wrong_guesses, "/6")

while "_" in hidden_word and wrong_guesses<6:
    guess = input("Guess a letter: ").upper()
    guessed_letters.append(guess)
    if guess in guessed_letters[:-1]:
        print("You've already guessed this letter.")
        continue

    if len(guess)!=1 or not guess.isalpha():
        print("enter one letter.")
        continue
    
    correct = False

    for index, letter in enumerate(secret_word):
        if letter == guess:
            hidden_word[index]=letter
            correct= True

    if not correct:
        wrong_guesses+=1

    print("word: ", " ".join(hidden_word))
    print("wrong guesses: ", wrong_guesses, "/6")
if "_" not in hidden_word:
    print("YOU WOOONNNNNNNNNNNN!!!!!!!!!!!!!!!!!")
else:
    print("AWWWWWW, YOU LOST")
    print("The word was", secret_word)