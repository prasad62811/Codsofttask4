import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice (rock, paper, scissors):")
    player_choice = input().lower()
    computer_choice = get_computer_choice()
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    print(determine_winner(player_choice, computer_choice))

# Main program loop
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
