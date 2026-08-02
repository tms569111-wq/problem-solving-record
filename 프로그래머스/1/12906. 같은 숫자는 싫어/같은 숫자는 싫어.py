def solution(arr):
    answer = [1000]
    for value in arr:
        if answer[-1] != value:
            answer.append(value)
    return answer[1:]