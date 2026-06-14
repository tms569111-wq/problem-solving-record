from collections import deque
# 약간 투 포인터 
# 근데 k 쓰니까약간 슬라이딩 윈도우스런느낌적인느낌

def solution(stones, k):
     # k구간을 담을 queue
    q=deque()
    # 큰놈들 중 제일 작은 놈
    min_stone=1e9
    # 이거 슬라이딩 윈도우로 집합 싹다 구하고
    # q에서 가는데 k크기 큐에서 max값이 전체 집합 중 가장 작은 놈이 정답
    # 이때 시간 복잡도 잡으려면...
    # local max하니까 case 13만 엣지케이스 시간초과...
    # while 문으로 한 칸 앞에 데이터가 맨 뒤보다 크면
    # 계속 맨앞 것을 빼야된다
    # 아 이거 안 되네
    # index로 보고 풀어야 곘다
    # index로 슬라이딩 윈도우 하고 슬라이딩 윈도우 하면서 작은 놈들 빼고 최대값만 따로 구하기.
    # 오!
    for i in range(len(stones)):
        if q and q[0]<=i-k:
            q.popleft()
        while q and stones[q[-1]]<=stones[i]:
            q.pop()
        q.append(i)
        if i>=k-1:
            min_stone=min(min_stone,stones[q[0]])
    return min_stone
        