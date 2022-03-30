import random
import string
import winsound
import pyperclip
import shutil
import os

def beep():
    winsound.Beep(1000,100)
    
info="""Enter the type of the password: 
    1 : Numbers
    2 : Letters
    3 : Mix 'Letters & Numbers'"""

def majpass():
    print(info)
    passtype=int(input())
    passize=int(input("Enter the size of the password : "))
    if passtype==1:
        rapass=[str(random.randint(0,9)) for i in range(passize)]
        #or string.digits
        # make an option to choose upper, lower, or both!
    elif passtype==2:
         rapass=[random.choice(string.ascii_letters) for i in range(passize)]

    elif passtype==3:
        rapass=[random.choice(string.ascii_uppercase+ string.digits) for i in range(passize)]

    else:
        print(f"please enter a valid number from the list below! you entered: '{passtype}'")
        majpass()
    rapass="".join(rapass)
    pyperclip.copy(rapass)
    open("pass.txt","w+").write(rapass)
    shutil.copy("pass.txt", os.path.join(os.environ["HOMEPATH"], "Desktop"))
    beep()
    print(rapass)
majpass()
