import math
def solution(n, m):
    a=math.gcd(n,m)
    b=n*m/a
    answer = [a,b]
    return answer