
def solution(n, costs):
    # 프림이나 크루스칼 알고리즘인데 
    # 아 이거 손으로 하면 엄청 쉬운데
    # 코드로 하려니까 막막하네
    parent = [i for i in range(n)]
    rank = [0] * n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
        
    def union(a,b):
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            return False
        parent[root_a] = root_b
        return True
        
        
        
    answer = 0
    edge_count = 0
    costs.sort(key = lambda x:x[2])
    for a, b, cost in costs:
        if union(a,b):
            edge_count += 1
            answer += cost
            if edge_count == n-1:
                break
    return answer

        
            