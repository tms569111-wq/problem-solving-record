from collections import deque
def solution(n):
    answer =deque([])
    
    for i in str(n):
        answer.appendleft(int(i))
    
    return list(answer)