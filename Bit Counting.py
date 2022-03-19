from typing import Counter
def count_bits(n):
    return Counter(bin(n))["1"]
