'''
Assertions are statements that assert or state a fact confidently in program.
Assertions are simply boolean expressions that checks if the condition return true or not.
If it is true, the program does nothing and move to the next line of code. However, if it's false, the program stops and throws an error.

assert statement has a condition or expression which is supposed to be always true.
If the condition is false assert halts the program and gives an AssertionError

syntax for using Assert in python
assert <conditon>
assert <condition>, <error message>
'''

# example
a = 3
assert a == 2, 'a is not 3'
 => it shows a error message 'a is not 3'
