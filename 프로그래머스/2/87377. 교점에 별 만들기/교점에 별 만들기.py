# 일단 n에 최대는 1000임
# n*2까지는 가능
# 처음에는 이게 뭔 소린가 싶었는데
# 걍 조합 느낌으로 line의 교점만 격자에 별로 표시하면 될 듯
# 먼저 2중 for문으로 주어진 교점의 공식을 이용해서 값을 구하고
# if 1.0 == int(1.0): True이나 if 1.1 == int(1.1):는 False인 걸 이용해서
# x, y가 둘다 정수면 리스트에 넣기
# 리스트 x랑 y를 정렬
# x, y가 제일 작은 놈이랑 x, y가 제일 큰놈
# 그것들 차이를 구하고 그 차이만큼 격자 생성
# 리스트 돌아가면서 차이만큼 더하고 그 위치에 별 생성
def solution(line):
    n = len(line)
    cross = set()
    max_X = -1e15
    max_Y = -1e15
    min_X = 1e15
    min_Y = 1e15
    for i in range(n):
        A, B, E = line[i]
        for j in range(i + 1, n):
            C, D, F = line[j]
            if (A * D - B * C) == 0:
                continue
            else:
                X = (B * F - E * D) / (A * D - B * C)
                Y = (E * C - A * F) /  (A * D - B * C)
                if X == int(X) and Y == int(Y):
                    X = int(X)
                    Y = int(Y)
                    max_X = max(max_X, X)
                    max_Y = max(max_Y, Y)
                    min_X = min(min_X, X)
                    min_Y = min(min_Y, Y)
                    cross.add((X, Y))
                    
    cross_list = list(cross)
    I = abs(max_X - min_X) + 1
    J = abs(max_Y - min_Y) + 1
    board = [["." for _ in range(I)] for _ in range(J)]
    
    for x, y in cross_list:
        x -= min_X
        y -= min_Y
        board[y][x] = "*"
    answer = []
    for i in range(len(board) - 1, -1, -1):
        answer.append("".join(board[i]))
        
    return answer