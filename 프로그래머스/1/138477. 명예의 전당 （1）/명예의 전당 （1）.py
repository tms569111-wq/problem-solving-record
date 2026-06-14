import heapq

def solution(k, score):
    q = [] 
    answer = []
    for s in score:
        heapq.heappush(q, s)
        if len(q) > k:
            heapq.heappop(q) 
        answer.append(q[0])
    return answer