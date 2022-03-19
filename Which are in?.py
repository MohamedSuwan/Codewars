def in_array(a1, a2):
    return sorted(set(i for i in a1 for j in a2 if i in j))
