import numpy as np
def snail(a):
    l=[]
    while len(a)>0:
        l.append(a[0])
        a=np.rot90(np.delete(a,0,0))
    return list(np.hstack(l))
