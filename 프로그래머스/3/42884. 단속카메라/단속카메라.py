from collections import deque
def solution(routes):
    routes.sort(key = lambda x : (x[1], x[0]))
    answer = 0
    routes = deque(routes)
    while routes:
        now = routes[0][1]
        while routes and now <= routes[0][1] and now >= routes[0][0]:
            routes.popleft()
        answer += 1
    return answer
        
   