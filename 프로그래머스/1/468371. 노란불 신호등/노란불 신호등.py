# 노란 불이 되는 구간
# 처음 든 생각은 최소공배수
# 그러나? 각 초가 다르므로 어렵다 5초 , 1초, 3초 이런식이면...
# 노란색 구간을 누적합으로 구한다
# 노란색 구간이 처음으로 n개가 될 때에 시점을 return
# 아니면 최소공배수를 20 * 5개 해서 100개 구하거나...
# 누적합하면 근데 어디까지 봐야 하는가. 끝나는 시간이 없지.
# 이럴 때는 모두가 한 바퀴 돌 때에
# 즉 20 ^ 5 400 * 400 16만 한 2000만번 해보고 안 되면 포기.
# 1 부터 20 사이에 소수들
# 2, 3, 5, 7, 11, 13, 17, 19
# Y가 1초인 경우가 19 * 17 * 13 * 11 * 7이 최악의 경우
# 귀찮으니까 대충 한 300만번 정도
# 노란색인지 판별하는 방법
# 첫 Y = G + 1 부터 Y = G+Y까지
# 그 뒤 Y는 첫 Y에서 G + Y + R한 거에다가 마지막 Y에다가 G + Y + R 한거
def solution(signals):
    n = len(signals)
    time = [0 for _ in range(3000000)]
    for G, Y, R  in signals:
        last_Y = G + Y
        first_Y = G + 1
        sum_signals = G + Y + R
        while last_Y < 3000000:
            for i in range(first_Y, last_Y + 1):
                time[i] += 1
            last_Y += sum_signals
            first_Y += sum_signals
    for i in range(3000000):
        if time[i] == n:
            return i
    answer = -1
    return answer