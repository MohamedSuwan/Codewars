from itertools import permutations as pp
def permutations(string):
    return ("".join(y) for y in(set(i for i in (pp(string)))))
