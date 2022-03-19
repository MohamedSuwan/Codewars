def DNA_strand(dna):
    a=[]
    for i in dna:
        if i =="A":
            a.append("T")
        elif i =="T":
            a.append("A")
        elif i =="G":
            a.append("C")
        else:
            a.append("G")
    return("".join(a))
