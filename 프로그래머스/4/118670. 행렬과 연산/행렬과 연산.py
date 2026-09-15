# 최악 수백 * 수백 * 10만...
# 시간이 너무 위험한데
# dp 같은 걸로 상태를 저장하나? 
from collections import deque
def solution(rc, operations):
    left = deque()
    right = deque()
    middle = deque()
    
    for row in rc:
        left.append(row[0])
        right.append(row[-1])
        middle.append(deque(row[1:-1]))
    
    for op in operations:
        if op == 'ShiftRow':
            left.rotate(1)
            middle.rotate(1)
            right.rotate(1)
        else:
            middle[0].appendleft(left.popleft())
            right.appendleft(middle[0].pop())
            middle[-1].append(right.pop())
            left.append(middle[-1].popleft())            
    answer = []
    for l, m, r in zip(left, middle, right):
        answer.append([l] + list(m) + [r])
    return answer