#https://www.codewars.com/kata/is-my-friend-cheating/train/python
# 1부터 n까지의 number를 갖고 있는 list를 만듬
# 해당 list에서 a와 b를 제외하고 모든 element를 더했을 때의 값이 a와 b를 곱했을 때의 값과 동일한 a와 b를 고르는 문제

def removNb(n):
    # 1~n까지 element를 가지고 있는 list의 sum 값을 구해야 하는데, sum함수를 사용하면 n값이 커질수록 구동속도 엄청 느려짐
    # 그래서 등차수열 공식 사용
    total = n * (n+1) / 2 
    result = list()
    # 1~n까지 element를 갖는 list에서 element를 한 개씩 빼오는건데, 1부터 n까지 차례대로 있는 list형태이므로 굳이 list 생성 안하고 range로 바로 생성해서 프로그래밍
    for a in range(1,n+1):
        b = ( total - a ) / (a+1)
        # b가 5.0 일 때 type(b)는 float이지만, is_integer() 함수 하면 ture로 나옴. 
        # 'if b in 리스트' 문법을 사용하면 리스트의 element들을 indexing 하므로, n값이 커질수록 엄청 느려짐
        # 따라서 b 값을 list에 있는지 일일이 찾으면 O(n)이 걸리는데, b값이 list안에 들어있는 적합한 값인지 check만 하면 O(1)이 걸림
        # 'a * b = sum값 - a - b' 가 되는 경우를 구해야 함. 
        # for loop 통해서 a값을 가져오면서 짝이 맞는 b 값을 구함. b값이 정수이고 n값보다 작으면 조건에 맞는 b값을 구한 것임
        # list 안에 있는 b 값을 구한 것이니까.
        if b.is_integer() and b <= n:
            result.append((a,int(b)))
    return result

removNb(1000003)
'''
import time
start = time.time()
end = time.time()
process_time = end - start
위와 같이 구동시간을 구할 수도 있으나, timeit 을 import 하면 이용할 수 있는 function이 여러개 있음. 나중에 알아보기
'''
