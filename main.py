from random import seed
from random import randint


print("welcome to the guessing game by voblog")

name = input("enter your nAme: ")
print(f"hello {name}!")

# pick a random number
seed()
n= randint(0,1000)
while True:
    # ask for a number
    guess=input("guess a number: ")
    g =int(guess)
    # check if it is right or not
    if g==n:
        print("correct! yay")
        break
    elif g > n:
        print("too high")
    else:
        print("too too low")