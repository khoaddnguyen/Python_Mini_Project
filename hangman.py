import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the word list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # keep track of which letter already being guessed in the chosen word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letter(s) used
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
        # current word status W-RD
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))


        guess_letter = input("Guess a letter: ").upper()
        if guess_letter in alphabet - used_letters:
            used_letters.add(guess_letter)
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)

            else:
                lives = lives - 1
                print("Letter is not in word.")

        elif guess_letter in used_letters:
            print("You have already guess that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # get here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You died. The word was", word, "!")
    else:
        print("You guess the word", word, "!!")

hangman()