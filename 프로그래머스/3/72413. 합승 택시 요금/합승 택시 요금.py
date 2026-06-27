def solution(n, s, a, b, fares):
    # 1. 합승하는 경우
    # 1-1 같이 가다가 중간에 내리는 경우
    # 1-2 도착점까지는 같이 가는 경우
    # 합승 안하는 경우 비교
    # 일단 s에서 그냥 a가는 경우 최솟값, s에서 그냥 b가는 경우 최소값 다익스트라나 다른 걸로 구하고
    # 합승이 문제 합승은 일단 a랑 b에서 겹치는 부분까지는 같이 갔다가 달라지는 부분부터 최솟값비교?
    
    INF = 10**15
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
    answer = INF
    for i in range(1, n + 1):
        cost = dist[s][i] + dist[i][a] +dist[i][b]
        answer = min(answer, cost)
    
    return answer