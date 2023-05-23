# Guess My Number
import random
from art import logo

EASY_MODE = 10
HARD_MODE = 5

def set_difficulty(difficulty):
    if difficulty == "easy":
        return EASY_MODE
    elif difficulty == "hard":
        return HARD_MODE
    else:
        print("Invalid difficulty!")
        return -1
        
def compare_numbers(player, random):
    if player == random:
        return [1, f"You guessed the correct number! The answer was {random}."]
    elif player > random:
        return [0, "Your guess is too high!"]
    elif player < random:
        return [0, "Your guess is too low!"]

def adjust_lives(lives, status):
    if status == 0:
        return lives - 1

# Main game function
def number_guessing_game():
    print(logo)
    print("Welcome to Guess My Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Ask player for difficulty until proper answer is given
    player_lives = -1
    while player_lives == -1:
        player_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        player_lives = set_difficulty(player_difficulty)
    
    # Generate random number
    random_number = random.randint(1, 100)
    
    # Allow player to guess the random number as long as they have lives left and check guess
    player_number = 0
    while player_number != random_number:
        print(f"You have {player_lives} attempts remaining to guess the number.")
        
        player_number = int(input("Guess a number: "))
    
        guess_status = compare_numbers(player_number, random_number)
        print(guess_status[1])
    
        player_lives = adjust_lives(player_lives, guess_status[0])
    
        if player_lives == 0:
            print("You have run out of guesses! You lose.")
            return
        elif player_number != random_number:
            print("Guess again.")

number_guessing_game()