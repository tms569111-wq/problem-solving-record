import sys
def solution(n, m, x, y, r, c, k):
    # bfs로는 구현이 어려울 듯 상하좌우 visited아닐 때도 해야 하는데
    # dfs가 맞음
    # 근데 k가 2500번
    # 재귀를 2500번 불가능하지 않나
    # 찾아보니 sys로 해결 가능
    # 아니네 시간이 4^2500 ;;;
    # 이거 그리디네
    dist = abs(x - r) + abs(y - c)
    if dist > k:
        return "impossible"
    
    if (k - dist) % 2 == 1:
        return "impossible"
    directions = [
        ("d", 1, 0), 
        ("l", 0, -1),
        ("r", 0, 1),
        ("u", -1, 0)
    ]
    answer = []
    
    cur_x, cur_y = x, y
    for step in range(k):
        for char, dx, dy in directions:
            nx = cur_x + dx
            ny = cur_y + dy
            
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            remain = k - step - 1
            next_dist = abs(nx - r) + abs(ny - c)
            if next_dist <= remain and (remain - next_dist) % 2 == 0:
                answer.append(char)
                cur_x, cur_y = nx, ny
                break
    return ''.join(answer)