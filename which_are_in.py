# https://www.codewars.com/kata/which-are-in/train/python

'''
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []
'''

def in_array(array1, array2):

    r = list()
    
    for i in array1:
        for j in array2:
            if i in j:
                r.append(i)
                break

    # duplicates 를 없애기 위해 r을 set으로 만들었다가 다시 list로 만들었음 list(set(r)) 그런데 이럴 필요 없음.
    #   -> set type을 sorted() 하면 sorted 된 list type을 return 함. sorted(r) 을 하면 r 자체는 안 변하고 sorted된 값을 return 함
    return sorted(set(r))

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']

in_array(a1, a2)

# ['arp' in s for s in a2]

'''best practice  내가 이해하기 쉽게 변수명만 조금 변경
# any built-in function: iterable 객체를 받아서 어느 하나라도 True이면 True를 return. 모두 다 False일 때만 False Return.
def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in a2_element for a2_element in a2) })
'''
