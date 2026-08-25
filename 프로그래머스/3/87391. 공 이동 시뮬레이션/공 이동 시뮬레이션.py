# 차라리 도착지점에서 거꾸로 했을 때에 가능한 시작점이 정답이 아닐까?

def solution(n, m, x, y, queries):
    min_x = max_x = x

    min_y = max_y = y

    for command, distance in reversed(queries):

        if command == 0:
            if min_y != 0:
                min_y += distance

            max_y = min(m - 1, max_y + distance)

        elif command == 1:
            min_y = max(0, min_y - distance)

            if max_y != m - 1:
                max_y -= distance

        elif command == 2:
            if min_x != 0:
                min_x += distance

            max_x = min(n - 1, max_x + distance)

        else:
            min_x = max(0, min_x - distance)

            if max_x != n - 1:
                max_x -= distance

        if min_x > max_x or min_y > max_y:
            return 0

    row_count = max_x - min_x + 1
    column_count = max_y - min_y + 1

    return row_count * column_count