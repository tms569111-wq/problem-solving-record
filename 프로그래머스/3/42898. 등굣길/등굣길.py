def solution(m, n, puddles):
    # m(가로), n(세로) -> 배열은 [n+1][m+1]로 만드는 게 편해요
    load = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 웅덩이 위치를 -1로 표시 (가로, 세로 좌표 주의!)
    for px, py in puddles:
        load[py][px] = -1
        
    # 시작점 설정
    load[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 시작점이거나 웅덩이이면 건너뛰기
            if (i == 1 and j == 1) or load[i][j] == -1:
                continue
            
            # 왼쪽(j-1)과 위쪽(i-1)에서 오는 경로 합치기
            # 이때 웅덩이(-1) 값은 0으로 취급해서 더함
            from_top = load[i-1][j] if load[i-1][j] != -1 else 0
            from_left = load[i][j-1] if load[i][j-1] != -1 else 0
            
            load[i][j] = (from_top + from_left) % 1000000007
            
    return load[n][m]
