from collections import deque
import heapq
def solution(jobs):
    answer = 0
    running = []
    for i in range(len(jobs)):
        jobs[i].append(i)
    jobs.sort(key = lambda x : (x[0], x[1], x[2]))
    q = deque(jobs)
    now_time = 0
    while q or running:
        while q and q[0][0] <= now_time:
            start, end, num = q.popleft()
            heapq.heappush(running, (end, start, num))
        
        if running:
            end, start, num = heapq.heappop(running)
            now_time += end
            answer += now_time - start
        else:
            now_time = q[0][0]
        
    return answer // len(jobs)