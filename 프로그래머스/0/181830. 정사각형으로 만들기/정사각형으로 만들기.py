def solution(arr):
    a,b=len(arr), len(arr[0])

    if a > b:
        for i in range(a):
            for j in range(a - b):
                arr[i].append(0)
        return arr
    elif a<b:
        for i in range(b-a):
            arr.append([0] * b)
        return arr
    else:
        return arr