# bfs로 현재 height보다 이하의 차이가 나는 경우는 append하고 아니면 냅두기...
# 근데??? 어떻게 할까...사다리를 여러개 만드나?
# bfs로 한 번은 높이 차가 나도 다른 곳으로 갈 때 높이 차가 안 날 수도 있고...
# 높이차가 안 나게 기껐 했더니만 걍 높이 차가 나도록 하는 게 더 좋을 수도 있지 않나???
# 아닌가 무조건 사다리 없이 갈 수 있는 게 좋나...
# 일단 bfs로 deque에다가 추가를 하는데
# 맨 처음 시작을 1이라고 해서 상태 1로 두면...
# 못 가는 놈 나올 때 못 가는 놈을 2로? 아니면 원소의 크기가 ....
# 10000정도니까 height로 나눠서....
# 아니지 현재 칸 기준이라서 1씩 계속 올라간다면 높이가 1만이 차이나더라도 사다리가 없을 수도...
# 그니까 현재 기준 갈 수 없는 놈이면 계속 상태를 1씩 올리고...
# 갈 수 있는 놈이면 걍 상태를 덮어 씌울까......
# 흠...근데 설치한 사다리는 제한이 없다라....철거도 없고....
# 걍 모든 칸 상태를 1e9로 둘까...
# start를 1로 두고 (내 경우에는 (1, 1))
# 이동할 때 어떤 칸의 상태가 현재 상태보다 크면 걍 1
# 못 가면 1 + 1
# 또 못 가면 1 + 2
# 또 못가나...싶었는데 이미 1인 상황이라면
# 굳이 4로 하지 않고 1로...
# 아니면 4로 두고 추가해야 하나?
# 대갈빡 아프네...
# 사다리는 edges = [(a, b, abs(dist[a] - dist[b]))]
# 로 두고 1부터 모든 것 다 크루스칼 하면 될 것 같긴 한데....
# a나 b는 원래 (1, 1)같은 형식인데 편하게 하려면 i * n + j하면 되겠고
# dist도...
# 일단 해보고 안 되면 더 좋은 생각을 내보자...

def solution(land, height):
    n = len(land)
    V = n * n
    size = [1] * (V)
    parent = list(range(V))
    edges = []
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != x:
            nxt = parent[x]
            parent[x] = root
            x = nxt
        return root
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a == root_b:
            return False
        
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
            
        parent[root_b] = root_a
        size[root_a] += size[root_b]
        
        return True
    

    for x in range(n):
        for y in range(n):
            now = x * n + y
            if x + 1 < n:
                nxt = (x + 1) * n + y
                diff = abs(
                    land[x][y] - land[x + 1][y]
                )
                if diff <= height:
                    cost = 0
                else:
                    cost = diff
                edges.append((cost, now, nxt))
            if y + 1 < n:
                nxt = x * n + y + 1
                diff = abs(
                    land[x][y] - land[x][y + 1]
                )
                if diff <= height:
                    cost = 0
                else:
                    cost = diff
                edges.append((cost, now, nxt))
                
    answer = 0
    count = 0
    edges.sort()
    for cost, a, b in edges:
        if union(a, b):
            count += 1
            answer += cost
        if count == V- 1:
            return answer