def solution(n, results):
    # 그래프라...
    # 감도 안 오네. 내가 학교에서 배운 그래프는 다익스트라나 bfs, dfs 벨만포드 무방향
    # 뭐 그런 것들인데 이건...
    # 모르겠다. 감도 안 오고 모르면 못 푸는? 그런 문제인듯
    answer = 0
    win = [[False] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        win[a][b] = True
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if win[i][k] == True and win[k][j] == True:
                    win[i][j] = True
    answer = 0
    
    for i in range(1, n + 1):
        known = 0
        
        for j in range(1, n + 1):
            if i == j:
                continue
            if win[i][j] or win[j][i]:
                known += 1
        if known == n - 1:
            answer += 1
    return answer