from collections import deque
def solution(food):
    answer=deque(['0'])
    for i in range(len(food)-1,0,-1):
        for _ in range(food[i]//2):
            answer.appendleft(i)
            answer.append(i)
    a=''
    for j in answer:
        a+=str(j)
    return a