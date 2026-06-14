def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        
        for j in range(queries[i][0], queries[i][1]+1):
            arr[j]=arr[j]+1
    return arr