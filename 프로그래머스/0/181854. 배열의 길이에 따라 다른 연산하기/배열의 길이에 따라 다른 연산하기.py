def solution(arr, n):
    z=len(arr)
    if len(arr)%2==1:
        for i in range(z):
            if i%2==0:
                arr[i]=arr[i]+n
    else:
        for i in range(z):
            if i%2==1:
                arr[i]=arr[i]+n
    return arr