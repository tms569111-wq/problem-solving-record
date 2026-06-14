def solution(a, b):
    answer = 0
    s=str(a)+str(b)
    answer = int(s)
    z=0
    z=2*a
    z=z*b
    if (z<answer):
        return answer
    else:
        return z