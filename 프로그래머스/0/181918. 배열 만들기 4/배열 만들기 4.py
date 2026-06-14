def solution(arr):
    i=0
    stk = [arr[i]]
    while(i<len(arr)):
        if stk==[]:
            stk.append(arr[i])
            i=i+1
        elif stk[-1]<arr[i]:
            stk.append(arr[i])
            i=i+1
        else:
            stk.pop()

    return stk