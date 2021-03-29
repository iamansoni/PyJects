import random

def gameWin(comp, you):
# if two value are equal, declare a tie!
    if comp == you:
        return None

# check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

# check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

# check for all possibilities when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer's Turn: Snake(s) Water(w) Gun(g)!!!")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) Gun(g): ")
result = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if result == None:
    print("The game is a tie!")
elif result == True:
    print("You Win!")
else:
    print("You Lose!")