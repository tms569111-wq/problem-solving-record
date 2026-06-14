def solution(num, k):
    a=str(num)
    k=str(k)
    if k not in a:
        return -1
    for i in range(num):
        if a[i]==k:
            return i+1
