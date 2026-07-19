import random 


def generate_answer():
    answers = [
        "Paper",
        "Rock",
        "Scissors"
    ]
    return random.choice(answers)

def main():
    print("Welcome to Rock, Paper, Scissors!")
    wins = 0
    loses = 0
    while True:    
        user_choice = input("Enter your choice (Rock, Paper, Scissors): Quit to (Q) ").capitalize()

        if user_choice == "Q":
            print("Thanks for playing!")
            break

        if user_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = generate_answer()
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            print("You win!")
            wins += 1
        else: 
            print("You lose!")
            loses += 1

        print(f"Wins: {wins}, Losses: {loses}")

if __name__ == "__main__":
    main()  