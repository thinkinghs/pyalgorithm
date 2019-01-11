def solution(number):
    # set comprehension, {}를 []로 바꾸면 list comprehension
    three = { i*3 for i in range(1, int(number/3)+1) if number != i*3 }
    five = { i*5 for i in range(1, int(number/5)+1) if number != i*5 }
    
    # three와 five set의 합집합
    result = sum(x for x in three|five)
    return result

solution(10)

# best practice in the website 문법적으로는 간단하지만 수학적으로는 O(n)이 너무 큼
def solution_simplecode(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
