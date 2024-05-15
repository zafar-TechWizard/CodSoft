import random
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def print_choices(user_choice, computer_choice):
    print(Fore.YELLOW + f"Your choice: {user_choice}")
    print(Fore.YELLOW + f"Computer's choice: {computer_choice}")

def print_score(round_number, user_score, computer_score):
    print(Fore.CYAN + f"       Round: {round_number}", end='     ')
    print(Fore.CYAN + f"       Your score: {user_score[0]}", end='     ')
    print(Fore.CYAN + f"       Computer's score: {computer_score[0]}")


def play_round(round_number, user_score, computer_score):
    print_score(round_number, user_score, computer_score)

    print(Fore.MAGENTA + "\nChoose one:")
    print(Fore.MAGENTA + "    1. Rock")
    print(Fore.MAGENTA + "    2. Paper")
    print(Fore.MAGENTA + "    3. Scissors")
    print(Fore.MAGENTA + "    4. Exit\n")
    user_choice = input(Fore.YELLOW + f"Your choice: ").lower()

    if user_choice == 'exit':
        print(Fore.YELLOW + "Thanks for playing! Final scores:")
        print(Fore.GREEN + f"Your score: {user_score[0]}")
        print(Fore.RED + f"Computer's score: {computer_score[0]}")
        return False

    if user_choice not in ['rock', 'paper', 'scissors']:
        print(Fore.RED + "Invalid choice! Please choose again.")
        return True

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print_choices(user_choice, computer_choice)

    result = winner(user_choice, computer_choice)
    print(Fore.CYAN + result)

    if result == "You win!":
        user_score[0] += 1
    elif result == "Computer wins!":
        computer_score[0] += 1

    return True

# ASCII art for decoration
print("\n" *2)
print(Fore.CYAN + "                Welcome to Rock-Paper-Scissors Game")
print(Fore.CYAN + "                ====================================")

user_score = [0]
computer_score = [0]
round_number = 0

while True:
    round_number += 1
    if not play_round(round_number, user_score, computer_score):
        break

    # Add a delay to make it more realistic
    time.sleep(1)
    print("\n"*2)