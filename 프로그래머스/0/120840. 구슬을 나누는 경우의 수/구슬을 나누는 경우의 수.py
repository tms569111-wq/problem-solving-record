def solution(balls, share):
    z=1
    if balls==1:
        return 1
    for i in range(1, balls+1):
        z=z*i
    for j in range(1, balls-share+1):
        z=z//j
    for k in range(1, share+1):
        z=z//k

    return z