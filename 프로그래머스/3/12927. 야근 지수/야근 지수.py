# 무조건 제곱이기 때문에 works가 큰 놈을 꺼꾸러 트려야 함
# 즉 계속해서 최대 값을 빼면 됨
# 즉 힙
import heapq
def solution(n, works):
    heap = []
    if n >= sum(works):
        return 0
    for i in works:
        heapq.heappush(heap, -i)
    while n > 0:
        now = heapq.heappop(heap)
        now += 1
        heapq.heappush(heap, now)
        n -= 1
    answer = 0
    for i in heap:
        answer += i * i
    return answer