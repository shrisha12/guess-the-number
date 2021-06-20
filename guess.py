import random
print("NUMBER GUESSING GAME")
number = random.randint(1,9)
chances = 0
times=int(input("enter how many chances you want:"))
print("GUESS A NUMBER(between 1 to 9):")
while chances<times:
    guess = int(input("ENTER THE NUMBER:"))
    if guess == number:
        print("CONGRATULATIONS!!!YOU WON!!")
        break
    elif guess<number:
        print("YOU GUESSED A LOW NUMBER:TRY FOR A HIGHER NUMBER",guess)
        chances=chnaces+1
    else:
        print("YOU GUESSED A HIGH NUMBER:TRY FOR A LOWER NUMBER",guess)
        chances=chances+1
if not chances<times:
    print("YOU LOST!! THE NUMBER IS",number)
