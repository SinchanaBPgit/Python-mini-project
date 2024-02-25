import random

def play():
    user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ")
    user_choice = user_choice.lower()

    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        return "It's a tie!"

    if is_win(user_choice, computer_choice):
        return "Congratulations! You win!"
