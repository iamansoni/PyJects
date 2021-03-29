import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess: \n"))
    guesses += 1
    if (userGuess == randNumber):
        print("You guessed it right!\n")
    else:
        if (userGuess > randNumber):
            print("You guessed it wrong! Enter a smaller number.\n")
        else:
            print("You guessed it wrong! Enter a larger number.\n")

print(f"You guessed the number in {guesses} guesses!\n")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses < hiscore):
    print("You have just broken the High Score!\n")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
