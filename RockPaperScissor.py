import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def get_user_choice():
    """Get the user's choice and validate it."""
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        user_input = input("Enter rock, paper, or scissors: ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
