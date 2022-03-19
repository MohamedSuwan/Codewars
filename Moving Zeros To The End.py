import numpy as np
def move_zeros(l):
    x=np.array(l)
    return list(np.concatenate((x[x!=0],(np.zeros(np.count_nonzero(x==0),dtype=int)))))
