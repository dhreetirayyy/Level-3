import random
import time
print("May I ask you for your name?") 
name = input()
def give_hint(guess, secret_number):
    if guess < secret_number:
        return "Hint: The number is higher than your guess."
    else:
        return "Hint: The number is lower than your guess."

def play_game(name):
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print(f"\nDear {name}, welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")
    
    while not guessed:
        try:
            guess = int(input(f"{name}, please enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue
            
            attempts += 1
            
            if guess == secret_number:
                guessed = True
                print(f"\nCongratulations, {name}! You guessed the number {secret_number}.")
                print(f"You took {attempts} attempt(s). Well done!\n")
            else:
                hint = give_hint(guess, secret_number)
                print(f"{hint}\n")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
play_again = True
while play_again:
    play_game(name)
    response = input("Do you want to play again? (yes/no): ").lower()
    if response != 'yes' and response != 'y':
        print(f"Thanks for playing, {name}! Goodbye!")
        play_again = False