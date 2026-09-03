def solution(numbers):
    INF = 1e9
    pos = {
        1: (0, 0), 2:(0, 1), 3: (0, 2),
        4: (1, 0), 5:(1, 1), 6: (1, 2),
        7: (2, 0), 8:(2, 1), 9: (2, 2),
        0: (3, 1)
    }
    def move(a, b):
        if a == b:
            return 1
        x1, y1 = pos[a]
        x2, y2 = pos[b]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        diagonal = min(dx, dy)
        straight = max(dx, dy) - diagonal
        return diagonal * 3 + straight * 2
    dp = [[INF] * 10 for _ in range(10)]
    dp[4][6] = 0
    for ch in numbers:
        target = int(ch)
        next_dp = [[INF] * 10 for _ in range(10)]
        for left in range(10):
            for right in range(10):
                if dp[left][right] == INF:
                    continue
                current = dp[left][right]
                if left == target:
                    next_dp[left][right] = min(
                        next_dp[left][right],
                        current + 1
                    )
                    continue
                if right == target:
                    next_dp[left][right] = min(
                        next_dp[left][right],
                        current + 1
                    )
                    continue
                next_dp[target][right] = min(
                    next_dp[target][right],
                    current + move(left, target)
                )
                next_dp[left][target] = min(
                    next_dp[left][target],
                    current + move(right, target)
                )
        dp = next_dp

    return min(min(row) for row in dp)