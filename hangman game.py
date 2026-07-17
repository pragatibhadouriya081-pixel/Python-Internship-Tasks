import random

words = ["apple", "mango", "Pragati", "Khushi", "water"]

word = random.choice(words)

guess_word = ""

for i in word:
    guess_word += "_"

chance = 6

print("Welcome to Hangman Game")

while chance > 0 and "_" in guess_word:

    print("\nWord :", guess_word)

    letter = input("Enter a letter : ").lower()

    if letter in word:

        new_word = ""

        for i in range(len(word)):
            if word[i] == letter:
                new_word += letter
            else:
                new_word += guess_word[i]

        guess_word = new_word
        print("Correct Guess")

    else:
        chance -= 1
        print("Wrong Guess")
        print("Chances Left :", chance)

if "_" not in guess_word:
    print("\nYou Won")
    print("Word was :", word)

else:
    print("\nYou Lost")
    print("Correct Word :", word)