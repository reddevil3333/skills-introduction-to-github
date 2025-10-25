# Rock, Paper, Scissors Game

A simple command-line Rock, Paper, Scissors game written in Python.

## How to Play

1. Run the game:
   ```bash
   python3 rock_paper_scissors.py
   ```

2. When prompted, enter your choice:
   - `rock`
   - `paper`
   - `scissors`
   - `quit` to exit the game

3. The computer will randomly choose its move, and the winner will be determined based on the classic rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock

4. The game keeps track of your score and continues until you type `quit`.

## Requirements

- Python 3.x

## Features

- Input validation
- Score tracking
- Clean, user-friendly interface
- Play multiple rounds
- Graceful exit with Ctrl+C or 'quit' command

## Example

```
========================================
Welcome to Rock, Paper, Scissors!
========================================

Rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock

Enter your choice (rock/paper/scissors) or 'quit' to exit: rock

You chose: rock
Computer chose: scissors
------------------------------
You win this round!

Score - You: 1 | Computer: 0 | Ties: 0
```

Enjoy the game!
