def solution(array):
    arr=[0,0]
    for i in range(len(array)):
        if array[i]>arr[0]:
            arr[1]=i
            arr[0]=array[i]

    return arr