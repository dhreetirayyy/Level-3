import random
playing = True
number = random.randint(0,15)
print("I will generate a number between 0 and 15.")
print("You can get 1 correct")
while playing:
    guess = int(input("Give your best guess:")) 
    if guess==number:
        print("You guessed correctly!")
        break
    else:
        print("Guess Again!")