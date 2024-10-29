import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def display_instructions():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("1. Choose 'rock', 'paper', or 'scissor'.")
    print("2. Rock beats scissor, scissor beats paper, and paper beats rock.")
    print("3. Type 'quit' to exit the game.")
    print("Let's start playing!\n")
def give_feedback(user_score, computer_score):
    if user_score > computer_score:
        print("Great job! You're on a winning streak!")
    elif user_score < computer_score:
        print("Don't worry! Keep trying, you can turn this around!")
    else:
        print("It's a close game! Let's see if you can pull ahead!")
def play_game():
    user_score = 0
    computer_score = 0
    display_instructions()
    while True:
        user_choice = input("\nYour choice (rock, paper, scissor, quit): ").lower()
        if user_choice == 'quit':
            print("\nFinal Scores:")
            print(f"Your Score: {user_score}\nComputer Score: {computer_score}")
            if user_score > computer_score:
                print("You Won!!!")
            elif user_score == computer_score:
                print("It's a Tie")
            else:
                print("You lose :(")
            print("Thanks for playing!")
            break
        if user_choice not in ['rock', 'paper', 'scissor']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose---> {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        give_feedback(user_score, computer_score)
    another_game = input("Do you want to play another round? (Y/N): ").lower()
    if another_game == "y":
        play_game()
    else:
        print("Thanks for playing!!!")
play_game()