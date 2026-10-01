def solution(n, results):
    # 그래프라...
    # 감도 안 오네. 내가 학교에서 배운 그래프는 다익스트라나 bfs, dfs 벨만포드 무방향
    # 뭐 그런 것들인데 이건...
    # 모르겠다. 감도 안 오고 모르면 못 푸는? 그런 문제인듯
    # 이건 플로이드 워셜
    
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for a, b in results:
        graph[a][b] = True
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == True and graph[k][j] == True:
                    graph[i][j] = True
    count = 0
    for i in range(1, n + 1):
        check = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            elif graph[i][j] == False and graph[j][i] == False:
                check = 1
                break
        if check == 0:
            count += 1
    return count
                