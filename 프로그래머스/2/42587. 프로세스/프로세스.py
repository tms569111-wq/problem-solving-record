from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    count = 0
    while True:
        max_pri = max(priorities)
        for _ in range(len(priorities)):
            if location == -1:
                location = len(priorities) - 1 
            
            if priorities[0] == max_pri and location == 0:
                return count + 1
            
            if priorities[0] != max_pri:
                left = priorities.popleft()
                priorities.append(left)
                location -= 1
                
            else:
                priorities.popleft()
                location -= 1
                count += 1
                break
                
            
                
                
                
                