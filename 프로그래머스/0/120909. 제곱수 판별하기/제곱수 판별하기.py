def solution(n):
    for i in range(n):
        if i*i<=n:
            if i*i==n:
                return 1
            continue
        else:
            break
    return 2