T = int(input())

for test_case in range(1, T + 1):
    N_matrix = list(map(int, input().split()))
    N = N_matrix[0]

    INF = 10**9
    dist = [[INF] * N for _ in range(N)]

    idx = 1

    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
            elif N_matrix[idx] == 1:
                dist[i][j] = 1

            idx += 1

    for k in range(N):
        for i in range(N):
            if dist[i][k] == INF:
                continue

            for j in range(N):
                if dist[k][j] == INF:
                    continue

                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    answer = min(sum(row) for row in dist)

    print(f"#{test_case} {answer}")