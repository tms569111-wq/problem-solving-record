import math
def solution(n):
    answer=-1
    x = math.sqrt(n)
    if x.is_integer():
        answer = (x+1)**2
    return answer