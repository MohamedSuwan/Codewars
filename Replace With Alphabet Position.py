def alphabet_position(text):
    return " ".join(str(ord(l)-96) for l in text.lower() if ord(l) > 96)
