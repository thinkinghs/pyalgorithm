# we can verify that the pairs of parentheses is right
# we can save the memory using chk variable instead of stack

def valid_parentheses(string):
    chk = 0
    
    for p in string:
        if p == "(":
            chk += 1
        elif p == ")":
            chk -= 1
        
        if chk < 0:
            return False
    
    return True if chk == 0 else False
