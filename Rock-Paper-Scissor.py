import random
useraction = int(input("Choose your choice 1.Rock 2.Paper 3.Scissors:")) 
if useraction==1: 
    userchoice="rock" 
elif useraction==2: 
    userchoice="paper" 
elif useraction==3: 
    userchoice="scissors" 
else: print("invaild input. Try Again") 
computeraction = random.randint(1,3) 
if computeraction==1: 
    computerchoice="rock" 
elif computeraction==2: 
    computerchoice="paper" 
elif computeraction==3: 
    computerchoice="scissors" 
print("Computer's choice:", computerchoice, "User's choice:", userchoice) 
print("Now we will compare the choices") 
if userchoice == "rock":
    if computerchoice == "paper":
        print("Computer wins! Paper covers rock.")
    elif computerchoice == "scissors":
        print("You win! Rock smashes scissors.")
    else:  
        print("Both chose the same choice. Play again")
elif userchoice == "paper":
    if computerchoice == "rock":
        print("You win! Paper covers rock.")
    else: 
        print("Computer wins! Scissors cuts paper.") 
elif userchoice=="scissors":
    if computerchoice=="paper": 
        print("You win! Scissors cuts paper.") 
    else:
        print("Computer wins!Rock smashes scissors.")
else: 
    print("Both chose the same choice. Play again")