def solution(sides):
    a,b=max(sides),min(sides)
    c=a+b-1
    x=a-b
    answer = c-x
    return answer