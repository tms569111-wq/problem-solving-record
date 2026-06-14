def solution(dots):
    def get_slope(p1, p2):
        return (p1[1] - p2[1]) / (p1[0] - p2[0])

    # 네 점을 두 개씩 짝짓는 3가지 경우의 수
    # 1. [0,1]과 [2,3]
    if get_slope(dots[0], dots[1]) == get_slope(dots[2], dots[3]):
        return 1
    # 2. [0,2]와 [1,3]
    if get_slope(dots[0], dots[2]) == get_slope(dots[1], dots[3]):
        return 1
    # 3. [0,3]와 [1,2]
    if get_slope(dots[0], dots[3]) == get_slope(dots[1], dots[2]):
        return 1
    return 0