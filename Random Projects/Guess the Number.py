import random
print("Welcome to 'Guess the Number' game")
print("i have a number between 1 and 333... can you guess it? \n")
print("if you want to Learn the game press 'l'")
print("if you want to PLAY the game press 'p'")
x=input()
if x=="l":
    print("c'mon its easy")
elif x=="p":
    ran=random.randint(1,333)

    for g in range (6):
        print(str(6-g)+" guesses left!")
        myg=int(input())
        if myg>ran:
            print("Guess lower")
        elif myg<ran:
            print("Guess higher")
        else:
            break
    if ran==myg:
        print("thats correct the number was "+str(ran)+" and you got it with only "+str(g+1)+" guesses!")
    else:
        print("sorry, you lost! the number was: " +str(ran))
else:
    print(':(')

