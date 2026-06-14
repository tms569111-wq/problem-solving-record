def solution(s):
    arr=s.split()
    answer=[]
    for i in arr:
        answer.append(int(i))
    a,b = max(answer),min(answer)
    return str(b)+' '+str(a)