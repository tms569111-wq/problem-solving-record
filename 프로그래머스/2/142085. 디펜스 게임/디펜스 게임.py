import heapq
def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        if n < 0 and k >= 1:
            n -= heapq.heappop(heap)
            k -= 1
        elif n < 0 and k == 0:
            return i
    return len(enemy)
    
            
            
            
    