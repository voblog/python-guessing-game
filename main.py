from random import seed
from random import randint

def gamerun(max, cheatmode=False):
    print("the game is starting yay")
    nguesses=0
    n= randint(0,max)
    min=0
    while True:
        # ask for a number
        if cheatmode:
            print(f"({min} - {max}) ", end='')
        guess=input("guess a number: ")
        g =int(guess)
        nguesses+=1
        # check if it is right or not
        if g==n:
            print(f"correct! yay it took you {nguesses} trys")
            break
        elif g > n:
            print("too high")
            if g <max:
                max=g
        else:
            print("too too low")
            if g >min:
                min=g


print("welcome to the guessing game by voblog")

name = input("enter your nAme: ")
print(f"hello {name}!")

# pick a random number
seed()
gamerun(1000,True)