def last_digit(n1, n2):
    if n1==10:
        return(0)
    else:
        return int(str(int(str(n1)[-1::])**int(str(n2)[-2::]))[-1])
