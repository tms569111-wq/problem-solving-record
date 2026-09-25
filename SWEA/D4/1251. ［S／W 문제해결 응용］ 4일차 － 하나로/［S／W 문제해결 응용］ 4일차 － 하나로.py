# 1000개인데 각 간선을 모두 구해야 함...
# 1000 +999 + ... + 1
# 1001 * 1000 / 2
# 50만
# 생각보다 널널하네....
# list에 50만개가 들어갈 수 있으니...
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e_money = float(input())
    edges = []
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    answer = 0
    for i in range(N):
        for j in range(N):
            if i == j or j < i:
                continue
            else:
                edges.append((i, j, abs(x[i] - x[j]) ** 2 + abs(y[i] - y[j]) ** 2))
    edges.sort(key = lambda x : x[2])
    def find(x):
        root = parent[x]
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
        if parent[root_a] == parent[root_b]:
            return False
        if parent[root_a] < parent[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]
        return True
    count = 0
    for a, b, c in edges:
        if union(a, b):
            count += 1
            answer += c
        if count == N - 1:
            break
    real_answer = int(answer * e_money + 0.5)
    print(f"#{test_case} {real_answer}")