from typing import Counter
def score(x):
    t=(Counter(x))

    def one(i,s):
        if i==5:
            s+=50
        elif i==1:
            s+=100
        return s

    def two(i,s):
        if i==5:
            s+=100
        elif i==1:
            s+=200
        return s

    def thr(i,s):
        if i==1:
            s+=1000
        else:s+=i*100
        return s
    
    s=0 
    we=0
    for i in t:
        if t[i]==1:
            we+=(one(i,s))
        elif t[i]==2:
            we+=(two(i,s))
        elif t[i]==3:
            we+=(thr(i,s))  
        elif t[i]==4:
            we+=(thr(i,s) + one(i,s))
        else:
            we+=(thr(i,s) + two(i,s))
    return(we)
