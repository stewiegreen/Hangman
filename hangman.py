from words import words as word
import random


def find_a_word():
    useable_word = random.choice(word)
    while "-" in useable_word:
        useable_word = random.choice(word)
    return useable_word


def check_user_input(user_input, word):
    if user_input in word:
        right_guesses.append(user_input)
        guesses.append(user_input)
        print(f"YES! '{user_input}' is in the word!\n")
        return True
    else:
        print(f"Sorry, '{user_input}' is not in this word\n")
        guesses.append(user_input)
        return False


def display_word(word, right_guesses):
    display = " "
    for letter in word:
        if letter in right_guesses:
            display = display + letter
        else:
            display = display + "-"
    return display


def play_again():
    useable_word = find_a_word()
    hangman(useable_word)


def hangman(useable_word):
    game_over = False
    chances = 8
    print("`~*Welcome to Hangman*~`\n")
    print(f"You have {chances} chances to guess the right word!\n")
    print("You're word is: " + display_word(useable_word, right_guesses) + "\n")
    while game_over == False:
        user_input = input("\nPlease choose a letter: ")
        while user_input in guesses:
            user_input = input(
                "That letter has been guessed, please choose a different letter: ")
        if check_user_input(user_input, useable_word) == False:
            chances = chances - 1
            print(f"You have {chances} chances left!")
            print("You're word is: " +
                  display_word(useable_word, right_guesses) + "\n")
            if chances == 0:
                game_over = True
                print("Sorry, You lose")
                print(f"The word was:  {useable_word}")
        else:
            if "-" not in display_word(useable_word, right_guesses):
                print(f"Congratulations! The word is {useable_word}\n")
                game_over = True
            else:
                print("You're word is: " +
                      display_word(useable_word, right_guesses) + "\n")
                pass

    restart = input("Would you like to play again?(y/n):  ")
    if restart == "y":
        guesses.clear()
        right_guesses.clear()
        play_again()
    else:
        quit


guesses = []
right_guesses = []
useable_word = find_a_word()
hangman(useable_word)
