# I use a filter built-in function.
# filter -> if condition is True in lambda, the element is returned.
# lambda 부분에서 구현된 statement가 true 이면 parameter로 받은 element를 return 해서 iterable 상태로 만듬
# filter를 list로 묶어주면 list형태로 변환됨.
# https://www.codewars.com/kata/array-dot-diff/train/python

def array_diff(a, b):
    return list(filter(lambda i: i not in b, a))

'''best practice
def array_diff(a, b):
    return [x for x in a if x not in b]
''''
