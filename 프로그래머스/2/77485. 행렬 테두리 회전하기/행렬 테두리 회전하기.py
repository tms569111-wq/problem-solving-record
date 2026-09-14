from collections import deque
def solution(rows, columns, queries):
    board = [[0 for _ in range(columns)] for _ in range(rows)]
    def rotate_border(board, x1, y1, x2, y2, k = 1):
        pos = []
        
        for y in range(y1, y2 + 1):
            pos.append((x1, y))

        for x in range(x1 + 1, x2 + 1):
            pos.append((x, y2))
        
        for y in range(y2 - 1, y1 - 1, -1):
            pos.append((x2, y))
        
        for x in range(x2 - 1, x1, -1):
            pos.append((x, y1))
        q = deque(board[x][y] for x, y in pos)
        
        q.rotate(k)
        min_value = 1e9
        for (x, y), value in zip(pos, q):
            board[x][y] = value
            min_value = min(value, min_value)
        return min_value
    count = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = count
            count += 1
    answer = []
    for x1, y1, x2, y2 in queries:
        answer.append(rotate_border(board, x1 - 1, y1 - 1, x2 - 1, y2 - 1, k = 1))
    return answer
        