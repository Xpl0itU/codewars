import re

def is_pangram(s):
    return len(set(re.sub('[^a-z]', '', s.lower()))) == 26