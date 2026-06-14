
def solution(n, costs):
    # 프림이나 크루스칼 알고리즘인데 
    # 아 이거 손으로 하면 엄청 쉬운데
    # 코드로 하려니까 막막하네
    parent = [i for i in range(n)]
    rank=[0] * n
    def find(x):
        root = x
        
        while parent[root] != root:
            root = parent[root]
        
        while parent[x] != x:
            next_x = parent[x]
            parent[x] = root
            x = next_x
        return root
    def union(a,b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a == root_b:
            return False
        
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] +=1
        return True
    costs.sort(key=lambda x:x[2])
    
    answer = 0
    edge_count = 0
    
    for a, b, cost in costs:
        if union(a,b):
            answer += cost
            edge_count += 1
        
        if edge_count == n-1:
            break
    return answer