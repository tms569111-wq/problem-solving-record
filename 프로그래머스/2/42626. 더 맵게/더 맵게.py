
import heapq
def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    count = 0
    while heap:
        if len(heap) == 1:
            if heap[0] >= K:
                return count
            return -1
        else:
            min_num = heapq.heappop(heap)
            min_num_2 = heapq.heappop(heap)
            if min_num >= K:
                return count
            else:
                heapq.heappush(heap, min_num + min_num_2 * 2)
            count += 1
    return -1