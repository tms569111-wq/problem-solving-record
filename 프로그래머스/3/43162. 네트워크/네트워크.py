from collections import defaultdict
def solution(n, computers):
    visited = [False] * n
    answer = 0
    def dfs(now):
        for i in range(n):
            if computers[now][i] == 1 and visited[i] == False:
                visited[i] = True
                dfs(i)
                
    for i in range(len(visited)):
        if visited[i] == False:
            visited[i] = True
            answer += 1
            dfs(i)
    return answer