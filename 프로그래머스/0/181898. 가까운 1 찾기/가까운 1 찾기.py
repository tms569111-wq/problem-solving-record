def solution(arr, idx):
    count=0
    for i in range(idx, len(arr)):
        if arr[i]==1:
            return i
    
    return -1