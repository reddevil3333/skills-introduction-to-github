#!/usr/bin/env python3
"""
Rock, Paper, Scissors Game
A simple command-line game where you play against the computer.
"""

import random
import sys


def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_player_choice():
    """Get the player's choice with input validation."""
    while True:
        choice = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()

        if choice == 'quit':
            return None

        if choice in ['rock', 'paper', 'scissors']:
            return choice

        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")


def determine_winner(player, computer):
    """Determine the winner of the round."""
    if player == computer:
        return "tie"

    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if winning_combinations[player] == computer:
        return "player"
    else:
        return "computer"


def display_result(player, computer, result):
    """Display the result of the round."""
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    print("-" * 30)

    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")


def play_game():
    """Main game loop."""
    print("=" * 40)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 40)
    print("\nRules:")
    print("  - Rock beats Scissors")
    print("  - Scissors beats Paper")
    print("  - Paper beats Rock")

    score = {'player': 0, 'computer': 0, 'ties': 0}

    while True:
        player_choice = get_player_choice()

        if player_choice is None:
            break

        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, result)

        # Update score
        if result == "tie":
            score['ties'] += 1
        elif result == "player":
            score['player'] += 1
        else:
            score['computer'] += 1

        # Display current score
        print(f"\nScore - You: {score['player']} | Computer: {score['computer']} | Ties: {score['ties']}")

    # Display final score
    print("\n" + "=" * 40)
    print("Game Over! Final Score:")
    print(f"You: {score['player']} | Computer: {score['computer']} | Ties: {score['ties']}")
    print("=" * 40)
    print("Thanks for playing!")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
