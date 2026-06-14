def solution(arr):
    max_1=1
    for i in range(len(arr)):
        if max_1<len(arr):
            max_1=max_1*2
        else:
            break
    k=max_1-len(arr)
    for i in range(k):
        arr.append(0)
    return arr