# 구간합 출력 문제
# 현재 위치에서 시간 지난 만큼 차지
# 이전에 했던 pip 카카오 문제랑 유사함
# 일단 작년 추석이니까 앞에 날짜는 무의미하고
# 처리시간은 시작과 끝 시간 포함이므로 
# 00:00:00.000 ~ 23:59:59.999
# 까지 시간을 구간합 슬라이딩 윈도우로 최대값 구하면 될 것 같은데
# 처리시간은 최대 3초인데 1000밀리초면 최대 3000
# 전체 로그데이터가 2000개
# 최대 6백만번 연산하고
# 이것도 너무 길면 그 끝에만 표시 해도 되긴 하겠군
# 근데 이건 시간이 더 길어서 이렇게 하면 시간 오바나겠네 걍 로그 데이터만 표시 해야지
# 그 뒤 1000 * 60 * 60 * 24
# 360만 * 24면 약 7천만...
# 흠...시간이 애매할 수도 있겠네...
# 일단 해볼까?
# 7천만번 연산하면 1400ms정도 걸리네 걍 할만 한 것 같기도 하고
# 일단 해보자
from collections import deque

def solution(lines):
    def time_to_ms(time):
        h, m, s = time.split(':')

        sec, ms = s.split('.')

        return (
            int(h) * 60 * 60 * 1000
            + int(m) * 60 * 1000
            + int(sec) * 1000
            + int(ms)
        )
    intervals = []
    for line in lines:
        day, time, duration = line.split(" ")
        end = time_to_ms(time)
        duration = duration[:-1]
        if '.' in duration:
            sec, ms = duration.split('.')
            ms = ms.ljust(3, '0')
            duration_ms = int(sec) * 1000 + int(ms)
        else:
            duration_ms = int(duration) * 1000
        start = end - duration_ms + 1
        intervals.append((start, end))
    answer = 0
    for _, window_start in intervals:
        window_end = window_start + 999
        count = 0
        for start, end in intervals:
            if start <= window_end and end >= window_start:
                count += 1
        answer = max(answer, count)
    return answer