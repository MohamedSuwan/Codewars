import re
def is_pangram(s):
    return len(set(re.findall("[a-z]",s.lower())))==26
