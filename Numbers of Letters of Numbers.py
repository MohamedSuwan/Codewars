w={
0:"zero",
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
}

def numbers_of_letters(n):
    l=[]
    word=""
    
    while True:
        for i in (str(n)):
            word+=w[int(i)]
        if n==4:
            l.append(word)
            break
        else: 
            n=len(word)
            l.append(word)
            word=""
    return (l)
