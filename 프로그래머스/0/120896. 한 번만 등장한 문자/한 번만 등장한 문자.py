def solution(s):
    a=[]
    check=[]
    for i in s:
        if i not in a and i not in check:
            a.append(i)
            check.append(i)
        elif i in a and i in check:
            a.remove(i)
    a.sort()
    a="".join(a)
    return a