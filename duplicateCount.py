# we can check the numbers of duplicated alphabets using Counter function

from collections import Counter

def duplicate_count(text):
    text= "abcdea"
    c = Counter(text.lower())
    result = list()
    
    for i in c:
        print(i)
        if c[i] >= 2:
            result.append(i)
    
    return len(result)
