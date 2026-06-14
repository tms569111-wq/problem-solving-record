def solution(binomial):
    a,b,c=binomial.split()
    a=int(a)
    c=int(c)
    if b=='+':
        answer=a+c
    elif b=='-':
        answer=a-c
    else:
        answer=a*c
    return answer