# bfs인 듯
# 조건만 까다롭지 크기는 조그마해서 할만 할 듯
# 상 하 좌 우 이동과 두 점 중 아무거나 축으로 해서 시계 반시계
# 총 8개 움직임
# 모든 점을 다 가도 시간복잡도는 넉넉할 듯
# 축으로 회전시 걸리는 걸 잘 예외처리 해야 될 듯.
from collections import deque
def solution(board):
    N = len(board)

    # ① 패딩
    new_board = [[1] * (N + 2)]

    for row in board:
        new_board.append([1] + row + [1])

    new_board.append([1] * (N + 2))

    board = new_board

    # ② 상태 정규화
    def make_state(p1, p2):
        return tuple(sorted([p1, p2]))

    def get_next(state):
        (x1, y1), (x2, y2) = state
        result = []

        # ③ 평행 이동
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for dx, dy in directions:
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy

            if (
                board[nx1][ny1] == 0
                and board[nx2][ny2] == 0
            ):
                result.append(
                    make_state(
                        (nx1, ny1),
                        (nx2, ny2)
                    )
                )

        # ④ 가로인지 판정
        if x1 == x2:
            for d in [-1, 1]:
                if (
                    board[x1 + d][y1] == 0
                    and board[x2 + d][y2] == 0
                ):
                    result.append(
                        make_state(
                            (x1, y1),
                            (x1 + d, y1)
                        )
                    )

                    result.append(
                        make_state(
                            (x2, y2),
                            (x2 + d, y2)
                        )
                    )

        else:
            for d in [-1, 1]:
                if (
                    board[x1][y1 + d] == 0
                    and board[x2][y2 + d] == 0
                ):
                    result.append(
                        make_state(
                            (x1, y1),
                            (x1, y1 + d)
                        )
                    )

                    result.append(
                        make_state(
                            (x2, y2),
                            (x2, y2 + d)
                        )
                    )

        return result

    start = make_state((1, 1), (1, 2))

    q = deque([(start, 0)])
    visited = {start}

    while q:
        state, count = q.popleft()

        if (N, N) in state:
            return count

        for next_state in get_next(state):
            if next_state not in visited:
                visited.add(next_state)
                q.append((next_state, count + 1))