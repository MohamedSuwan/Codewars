
from typing import Counter
def is_triangle(a, b, c):
    tl=(sorted([a,b,c]))
    if not(any(tl)>1):
        if tl[0]+tl[1]>tl[2]:
            return True
        else:
            return False
    else:
        return False
