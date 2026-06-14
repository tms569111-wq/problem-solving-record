from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    queue=deque([(begin,0)])
    visited=set()
    
    while queue:
        current, count= queue.popleft()
        if current==target:
            return count
        for word in words:
            if word not in visited:
                diff=0
                for i in range(len(word)):
                    if current[i]!=word[i]:
                        diff+=1
                if diff==1:
                    visited.add(word)
                    queue.append((word,count+1))
    return 0