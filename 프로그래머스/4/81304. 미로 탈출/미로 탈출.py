# 함정이 10개 이므로 2** 10 = 4 ** 5 = 16 * 16 * 4 = 800개 정도 미리 만들어 두기
# 흠...근데 800개가 3000개면.......
# 240만개....
# 여전히 괜찮나?
# 복잡하게 할 필요 없이 함정만 incoming과 outcoming해서
# 아니 이거 graph dic으로 하면...
# incoming할 때 애들도 다 바꿔야 되서 오히려 헷갈림.
# dfs로 3000개...
# 근데 흠...갔던 곳을 다시 밟을 수도 있다라...
# dijkstra?
# 저장해야 할 거 현재 발동된 함정 개수
# 현재 비용이랑 현재 위치...
# 비용은 그냥 위치만으로 저장하면 안 됨. 발동 함정 포함...
# 아니지 다르게 생각해
# 함정을 밟았어.
# 그러면 함정의 incoming과 아웃 comuing이 바뀌고
# 함정이랑 연결 된 놈들을 체크 할 때 원래 incoming에 있으면...outcoming으로
# outcoming에 있으면 incoming으로 하면 되지...
# 그러니까 어떤 함정이 역으로 되서 함정에서 갈 수 있는 곳을 다 가면
# 그 놈들은 전부 함정으로 못 가니까 함정 상태를 저장하면 함정만 빼면 되고
# 그놈들 말고 딴 놈 중에 원래 outcoming에 함정이 있으면 못 가게 하고
# outcoming에 함정이 없는데 incoming에 있었으면...가게 하고
# outcoming에도 없고 incoming에도 없으면 걍 가기...
# 와 졸라 복잡하네....
# 서로 다른 두 방 사이에 직접 연결된 길이 여러 개 존재할 수도 있습니다. 이것도 난감하고...
# dist는 담은 trap의 합으로 나타낸다.
from collections import defaultdict
import heapq
def solution(n, start, end, roads, traps):
    INF = float('inf')
    trap_idx = {}
    for i, trap in enumerate(traps):
        trap_idx[trap] = i
    graph = [[] for _ in range(n + 1)]
    for s, e, cost in roads:
        graph[s].append((e, cost, 0))
        graph[e].append((s, cost, 1))
    max_mask = 1 << len(traps)
    dist = [
        [INF] * max_mask
        for _ in range(n + 1)
    ]
    dist[start][0] = 0
    heap = [(0, start, 0)]
    while heap:
        cost, now, mask = heapq.heappop(heap)
        
        if cost > dist[now][mask]:
            continue
        
        if now == end:
            return cost
        
        for nxt, weight, direction in graph[now]:
            now_active = 0
            if now in trap_idx:
                bit = trap_idx[now]
                if mask & (1 << bit):
                    now_active = 1
            nxt_active = 0
            if nxt in trap_idx:
                bit = trap_idx[nxt]
                if mask & (1 << bit):
                    nxt_active = 1
            reversed_edge = now_active ^ nxt_active
            if direction != reversed_edge:
                continue
            new_mask = mask
            if nxt in trap_idx:
                bit = trap_idx[nxt]
                new_mask ^= (1 << bit)
            new_cost = cost + weight
            if new_cost < dist[nxt][new_mask]:
                dist[nxt][new_mask] = new_cost
                heapq.heappush(
                    heap, (new_cost, nxt, new_mask)
                )
            