# s로 string을 "abcde" 받으면 "A-Bb-Ccc-Dddd-Eeeee" 로 return 해줌
def accum(s):
    # comprehensive for문이 list로 return 해주고, join 함수가 list 사이 사이에 '-'를 삽입해줌 
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
