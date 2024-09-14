import random

def get_user_choice():
    print("Choose your move")
    print("1. Rock\n2.Paper\n3.Scissors")
    return int(input("Enter the corresponding number (1/2/3):"))

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "you win!"
    else:
        return "you lose!"

def display_result(user_choice,computer_choice, result):
    print(f"you chose{choices[user_choice]}, and the computer chose{choices[computer_choice]}.")
    print(result)

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice,computer_choice)
        display_result(user_choice,computer_choice, result)

        if "win" in result:
            user_score += 1

        elif "lose" in result:
            computer_score += 1

        rounds += 1

        play_again = input("Do you want to play again? (yes/no):").lower()
        if play_again != "yes":
            print(f"Thanks for playing! Final score - You: {user_score},computer: {computer_score}, Rounds: {rounds}")
            break

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
play_game()
