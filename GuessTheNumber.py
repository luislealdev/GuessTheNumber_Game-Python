import random
from Art import logo, author

print(logo)
print(author)

gameMode = input("Select mode of game (easy,hard): ")
hasWon = False
randomNumber = random.randint(1,100)


if gameMode=="easy":
    print("You have 10 lifes")
    lifes=10
else: 
    print("You have 5 lifes")
    lifes=5

while(not hasWon and lifes>0):
    numberByUser = int(input("Enter a number: "))
    if(numberByUser==randomNumber): hasWon = True
    else:
        if numberByUser<randomNumber: 
            print("Too low")
        else:
            print("Too high")
        lifes-=1

if(hasWon): print("Congratulations! You have won")
else: print("Sorry :( You lost")