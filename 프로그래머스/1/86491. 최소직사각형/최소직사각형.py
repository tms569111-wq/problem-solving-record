def solution(sizes):
    a=[]
    b=[]
    for i,w in sizes:
        if i>w:
            a.append(i)
            b.append(w)
        else:
            b.append(i)
            a.append(w)
    answer = max(a)*max(b)
    return answer