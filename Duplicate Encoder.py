def duplicate_encode(word):
    word=word.lower()
    i=set(word)
    t=[]
    n=[]
#     if there is more than one letter make a list of them letters
    [t.append(y) for y in i if word.count(y)>1]
#     replace thw letter with the replacement letter
    [n.append(")") if i in(t) else n.append("(") for i in word] 
    return("".join(n))
