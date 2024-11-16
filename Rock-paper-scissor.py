import random

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Function to play one round of the game."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: rock, paper, or scissors")

    user_choice = input("Enter your choice: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return None, None

    computer_choice = get_computer_choice()
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result, computer_choice

def main():
    user_score = 0
    computer_score = 0

    while True:
        result, _ = play_game()

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScores: You - {user_score} | Computer - {computer_score}")
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Final scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
