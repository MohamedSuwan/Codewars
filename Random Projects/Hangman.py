hanged="""
          |
          |
        __|__
       [|X X|]
        |___|
          |
         /|\\
        / | \\
       *  |  *
          |
         / \\
        /   \\
       /     \\
      *       *
"""
hanged=hanged.split("\n")
word="hehehehe"
wdic={i:j for i,j in enumerate(word)}
wdisplay={i:"*" for i in range (len(word))}
print(f"Guess the word, it's {len(word)} characters long!","\n")
guesses=[]
inc=0
for i in range(8+len(word)):
    guess=str(input("Enter your guess: "))
    guesses.append(guess)

    if guess not in wdic.values():
        inc+=2
        if inc==18:
            print("Sorry you lost! the word was: ",word)
            break

    else:
        for x in wdic.keys(): 
            if wdic[x]==guess:
                wdisplay[x]=guess 

    if wdic==wdisplay:
        print("Correct the word is: ",word)
        break

    print("\n".join(hanged[0:inc]),"\n")
    print(f"The word is: {''.join(wdisplay.values())}")
    print(f"You tried: {guesses}")
