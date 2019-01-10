def factory(x):
    return lambda arr:list(map(lambda i: i*x,arr))

# first = factory(5)
# test_arr = [1, 2, 3]
# first(test_arr) -> returns [5, 10, 15]
# 파이썬은 모든 것이 object. function도 object이다. function으로도 return 가능
''' factory(5)를 하면 아래와 같은 함수가 리턴 됨
def aaa(arr):
  return list(map(lambda i: i*5, arr))

map함수는 map(function, iterator, ....) 방식으로 사용
iterator들에서 한번에 element 한개씩 function으로 parameter 넘겨줌
작업이 다 끝나면 iterator object 형태로 return 해줌. list가 이 parameter를 받아서 list형태로 만듬
