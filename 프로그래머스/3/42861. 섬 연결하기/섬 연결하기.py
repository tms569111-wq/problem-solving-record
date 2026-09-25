
def solution(n, costs):
    # 프림이나 크루스칼 알고리즘인데 
    # 아 이거 손으로 하면 엄청 쉬운데
    # 코드로 하려니까 막막하네
    parent = list(range(n + 1))
    costs.sort(key = lambda x : x[2])
    size = [1] * (n + 1)
    answer = 0
    count = 0
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
        size[root_b] += size[root_a]
        parent[root_b] = root_a
        return True
    for a, b, cost in costs:
        if union(a, b):
            answer += cost
            count += 1
        if count == n - 1:
            return answer
            
    
    