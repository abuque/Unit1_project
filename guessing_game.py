"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    solution = random.randint(1,15)
    guesses = 0
    play = True
    while play:
        guesses += 1
        print("To quit enter 'q'")
        guess = input("Guess a number between 1-15:> ")
        if guess.lower() == 'q':
            print("\nThanks for playing\nGood Bye")
            break
        try:
            guess = int(guess)
            if guess == solution:
                clear_screen()
                print("!!!! You have guessed correctly !!!\n" \
                      "\n" \
                      "Your guess: {}\n" \
                      "Number of guesses: {}".format(solution,guesses))
                play = False
            elif guess not in range(1,16):
                clear_screen()
                print("Your guess is not between 1-15\n" \
                      "try again \n")
            elif guess > solution:
                clear_screen()
                print("!!Try guessing lower!!\n")
                continue
            elif guess < solution:
                clear_screen()
                print("!!Try guessing higher!!\n")
                continue

        except ValueError:
            print("Try again... Please enter a number\n")
            continue
    else:
        print()
        if input("Would you like to play again? y/n >").lower() != 'n':
            clear_screen()
            start_game()
        else:
            print("\nThanks for playing\nGood Bye")



welcome_msg = "Welcome to the Guessing Game!!\n"\
              "Where gussing is fun!!!\n"\
              "High Score: 2 guesses\n"
print(welcome_msg)

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
