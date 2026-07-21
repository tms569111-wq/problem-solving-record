# 5만개에서 n개씩 제거하면서 지점사이의 거리의 최솟값 중에 가장 큰 값
# 이거는 뭐 그리디고 뭐고 방법이 없이 전부 탐색하는 것 말고는 방법이 없어 보임
# 문제는 단순 무식한 길이
# 5만Cn * 50000인데 딱 봐도 시간 오바하기 쉬움
# nlogn으로 줄여야 함
# 문제의 카테고리는 이분 탐색
# 근데 내 개인적인 생각에는 그냥 모든 최소 거리 미리 구해두고
# 없어졌을 때 인덱스에서 없어진 곳 뛰어넘은 거리만 더한 것들을 구하면
# 2n = 10만 정도로 될 것 같은데
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left = 1
    right = distance
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        prev = 0
        for rock in rocks:
            gap = rock - prev
            if gap < mid:
                removed += 1
            else:
                prev = rock
        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer