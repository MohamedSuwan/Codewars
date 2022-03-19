def order_weight(s):
    n=((sum(int(x) for x in i),i) for i in s.split(" "))
    return " ".join(i[1] for i in sorted(n))
