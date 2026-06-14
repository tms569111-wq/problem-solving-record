# bfs, dfs, dp 중 어느쪽?
# 일단 수학적으로는 최대값을 빼는 게 제일 좋음.
#계속 최대값만 빼서 다시 리스트에 넣으면 시간 복잡도 개 오바
# deque나 최대 힙... deque에서는 sort하고 값 빼서 맨 오른쪽보다 작아지면 ...근데 이건 2개만 됨.
# 최대힙같은데...최대힙 어캐 구현 하는지 모름
# 씨발 배우면 되겠지 근데 언제 배우냐...
import heapq
def solution(n, works):
    if sum(works)<=n:
        return 0
    
    max_heap=[]
    for w in works:
        heapq.heappush(max_heap,-w)
    for _ in range(n):
        max_val=heapq.heappop(max_heap)
        heapq.heappush(max_heap,max_val+1)
    answer=sum(w**2 for w in max_heap)
    # works를 최대 힙으로 만든다
    # 최대힙의 최대값을 -1빼고 다시 최대힙 정렬한다.
    # n도 1뺀다.
    # n=0되었을 때에 모든 원소 제곱값을 answer로 만들어서 반환.

    return answer