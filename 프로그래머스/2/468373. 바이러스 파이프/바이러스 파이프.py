from collections import deque
import sys

# 최대 행동수가 10번이며 n도 100개다.
# 만약 어떤 a, b,c 중 1개를 연다면, 그 다음에 다시 같은 걸 여는 것은 의미없는 짓이다.
# 따라서 3 * 2 * 2 ... 2 해서 2^9 * 3이면 4 * 4 * 4* 4 * 6 = 16 * 16 * 6 = 96 * 16 = 1500 * 100번 
# 따라서 15만번이면 됨.
# 심지어 edges를 다 곱해도 1500만번임
# 완전탐색을 해야 한다.
# 이 경우는 재귀함수...
# 완전탐색 하는 게 나을 듯?
# dfs인가.
# 일단 보자고
# 일단 전체 상태 n이 주어지고 
def solution(n, infection, edges, k):
    n_now = [0 for _ in range(0, n + 1)]
    n_now[infection] = True
    answer = [0]
    A_list = []
    B_list = []
    C_list = []
    for i in range(len(edges)):
        if edges[i][2] == 1:
            A_list.append(edges[i])
        elif edges[i][2] == 2:
            B_list.append(edges[i])
        else:
            C_list.append(edges[i])
    def bfs(n_now_status_bfs, infection_now, type_now):
        if type_now == 1:
            pipe_list = A_list
        elif type_now == 2:
            pipe_list = B_list
        else:
            pipe_list = C_list
        
        q = deque(infection_now) 
        visited = [False for _ in range(n + 1)]
        
        
        for num in infection_now: 
            visited[num] = True
                
        while q:
            now = q.popleft() 
            for x, y, pipe_type in pipe_list:
                if x == now:
                    nxt =y
                elif y == now:
                    nxt = x
                else:
                    continue
                if not visited[nxt]:
                    visited[nxt] = True
                    n_now_status_bfs[nxt] = True
                    q.append(nxt)
        return n_now_status_bfs
    def dfs(n_now_status, k_now, type_now):
        if k_now == k:
            answer.append(sum(n_now_status))
            return
        infection_now = []
        for i in range(1, n + 1):
            if n_now_status[i] == 1:
                infection_now.append(i)
        n_now_status = bfs(n_now_status, infection_now, type_now)
        if type_now == 1:
            
            dfs(n_now_status.copy(), k_now + 1, 2)
            dfs(n_now_status.copy(), k_now + 1, 3)
        elif type_now == 2:
            dfs(n_now_status.copy(), k_now + 1, 1)
            dfs(n_now_status.copy(), k_now + 1, 3)
        else:
            dfs(n_now_status.copy(), k_now + 1, 1)
            dfs(n_now_status.copy(), k_now + 1, 2)
            
    dfs(n_now.copy(), 0, 1)
    dfs(n_now.copy(), 0, 2)
    dfs(n_now.copy(), 0, 3)
    
    return max(answer)