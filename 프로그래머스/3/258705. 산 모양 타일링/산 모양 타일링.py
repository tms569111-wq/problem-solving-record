def solution(n, tops):
    MOD = 10007
    
    prev2 = 1
    prev1 = 1
    for i in range(1, 2 * n + 1):
        has_top = (i % 2 == 1 and tops[i//2] == 1)
        if has_top:
            current = 2 * prev1 + prev2
        else:
            current = prev1 + prev2
        current %= MOD
        prev2 = prev1
        prev1 = current
    return prev1