def validate_pin(pin):
    #return true or false
    if len(pin) not in (4,6):
        return False 
    else:
        return len(list(filter(lambda x:str.isdigit(x), pin)))in (4,6)
