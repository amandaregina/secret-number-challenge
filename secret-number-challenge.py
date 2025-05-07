import random
import os
import winsound
from colorama import init, Fore, Style
init(autoreset=True)

SCORES_FILE = "scores.txt"

def play_win_sound():
    winsound.Beep(1000, 300)
    winsound.Beep(1200, 300)

def play_lose_sound():
    winsound.Beep(500, 600)

def save_score(name, score):
    with open(SCORES_FILE, "a") as file:
        file.write(f"{name} - {score}\n")

def load_top_scores(limit=5):
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r") as file:
        lines = file.readlines()
        scores = []
        for line in lines:
            try:
                name, score = line.strip().split(" - ")
                scores.append((name, int(score)))
            except:
                continue
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:limit]

def print_top_scores():
    top_scores = load_top_scores()
    if not top_scores:
        print(Fore.YELLOW + "No scores yet. Be the first to play!\n")
    else:
        print(Fore.CYAN + "🏆 Top Scores:")
        for i, (name, score) in enumerate(top_scores, start=1):
            print(f"{i}. {name} - {score}")
        print()

def guess_the_number():
    print(Fore.MAGENTA + "🎮 Welcome to the guessing game!")
    print_top_scores()
    player_name = input(Fore.CYAN + "Enter your name: ")
    print(Fore.GREEN + "\nChoose a difficulty level:")
    print("1 - Easy (1–10, 5 attempts, 50 points)")
    print("2 - Medium (1–100, 7 attempts, 100 points)")
    print("3 - Hard (1–1000, 10 attempts, 150 points)")
    
    while True:
        difficulty = input("Enter 1, 2 or 3: ")
        if difficulty == "1":
            range_max = 10
            max_attempts = 5
            max_score = 50
            break
        elif difficulty == "2":
            range_max = 100
            max_attempts = 7
            max_score = 100
            break
        elif difficulty == "3":
            range_max = 1000
            max_attempts = 10
            max_score = 150
            break
        else:
            print(Fore.RED + "Invalid choice. Please choose 1, 2, or 3.")
    
    secret_number = random.randint(1, range_max)
    attempts = 0
    score = max_score
    
    while attempts < max_attempts:
        try:
            guess = int(input(Fore.CYAN + f"\nAttempt {attempts + 1}/{max_attempts} - Guess the number (1–{range_max}): "))
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")
            continue
        
        attempts += 1
        if guess < secret_number:
            print(Fore.YELLOW + "🔼 The number is higher!")
        elif guess > secret_number:
            print(Fore.YELLOW + "🔽 The number is lower!")
        else:
            print(Fore.GREEN + f"\n🎉 Congratulations, {player_name}! You guessed the number {secret_number} in {attempts} attempts.")
            print(Fore.CYAN + f"🏆 Your score: {score}")
            save_score(player_name, score)
            play_win_sound()
            return True
            
        score = max_score - (attempts * (max_score // max_attempts))
    
    print(Fore.RED + f"\n💥 Game over, {player_name}! The secret number was {secret_number}.")
    print(Fore.RED + "💔 Better luck next time!")
    play_lose_sound()
    return False

def main():
    while True:
        guess_the_number()
        print()
        print(Fore.GREEN + "\nDo you want to play again? (y/n): ", end="")
        play_again = input().strip().lower()
        if play_again != "y":
            print(Fore.CYAN + "\nThanks for playing! See you next time. 👋")
            break

# Start the game
main()