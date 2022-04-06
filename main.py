import  random

GuessNumber= int(input("Enter a GuessNumber 1-10: "))

randomNumbers =random.randrange(1,10)

if GuessNumber == randomNumbers:
    print("Your have won")
else:
    print("You have loose the game")
