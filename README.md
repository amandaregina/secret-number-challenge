# Secret Number Challenge 🎮

## Overview
The Secret Number Challenge is an interactive number guessing game with colorful interface, sound effects, and a scoring system. Players try to guess a randomly generated secret number within a specified range, with different difficulty levels and scoring mechanisms.

## Features
- 🎯 Three difficulty levels:
  - Easy: Numbers 1-10 (5 attempts, 50 points)
  - Medium: Numbers 1-100 (7 attempts, 100 points)
  - Hard: Numbers 1-1000 (10 attempts, 150 points)
- 🎨 Colorful console interface using colorama
- 🔊 Sound effects for winning and losing
- 🏆 Score tracking system with persistent storage
- 📊 Top 5 high scores display
- ⭐ Dynamic scoring based on number of attempts
- 🔄 Option to play multiple rounds

## Requirements
- Python 3.x
- colorama
- winsound (Windows only)

## Installation
1. Clone this repository
2. Install the required package:
```bash
pip install colorama
```
3. Run the game:
```bash
python secret-number-challenge.py
```

## How to Play
1. Enter your name when prompted
2. Choose a difficulty level (1-3)
3. Try to guess the secret number within the given number of attempts
4. Get feedback after each guess (higher/lower)
5. Your score decreases with each attempt
6. View your score and the top 5 scores
7. Choose to play again or exit

## Scoring System
- Each difficulty level has a maximum score:
  - Easy: 50 points
  - Medium: 100 points
  - Hard: 150 points
- Score decreases with each attempt
- Top 5 scores are saved and displayed

## Project Structure
- `secret-number-challenge.py`: Main game file
- `scores.txt`: File storing high scores

## Note
This game uses the `winsound` module which is Windows-specific. For other operating systems, you may need to modify the sound implementation.