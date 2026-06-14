def solution(arr):
    answer=[arr[0]]
    for i in range(len(arr)):
        if i>0 and arr[i]!=arr[i-1]:
            answer.append(arr[i])
    return answer