import random
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 10
USER_PROMT = "Guess a number between {} and {}: \n"

while True:
    randomNumber = random.randint(LOWEST_NUMBER,HIGHEST_NUMBER)
    userGuess = 0

    while randomNumber != userGuess:
        userGuess = int(input(USER_PROMT.format(LOWEST_NUMBER,HIGHEST_NUMBER)))
    
        print("You guess:", userGuess)
        if randomNumber > userGuess:
            print("the number is higher!")
        elif randomNumber < userGuess:
            print("the number is lower!")
            
    print("you are correct! Yay!")

    print("")
    playAgain = input("Do you want to play again? y/n ")
    if playAgain == 'n':
       break