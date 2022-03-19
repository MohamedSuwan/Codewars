def narcissistic( value ):
    return sum(map(lambda x: x**(len(str(value))), map(int, (str(value))))) == value
