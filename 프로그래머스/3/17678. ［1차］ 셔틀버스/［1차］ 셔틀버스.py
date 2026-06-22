from collections import deque
def solution(n, t, m, timetable):
    # 각 시간 당 갈 수 있는 것을 계산 하자
    # 일단 n개의 셔틀버스랑 n시간에서의 셔틀버스를 계산해야 함.
    # 계산 하기 쉽게 모든 문자열을 일단 숫자로 변경 해야 함.
    # 다행히 시간복잡도는 제법 여유롭다.
    # 구현 관련 시뮬레이션 문제군.
    # 일단 시간부터.
    # 부분합 쓰면 뭔가 쉬울 것 같음
    start = 60 * 9
    
    answer = ''
    def time_int_to_str(t):
        a = str(t // 60)
        b = str(t % 60)
        if len(a) == 1:
            a = '0' + a
        if len(b) == 1:
            b = '0' + b
        return a + ":" + b
    def time_str_to_int(time):
        a, b = time.split(":")
        return int(a) * 60 + int(b)
    int_time = []
    for time in timetable:
        int_time.append(time_str_to_int(time))
    check_bus = []
    for i in range(n):
        check_bus.append(start + t * i)
    int_time.sort()
    man_list = []
    num = len(timetable)
    idx = 0
    last_crew = -1
    for i in range(len(check_bus)):
        # 버스 시간마다 부분합
        # 부분합에서다가 m빼야 함
        count = 0
        
        while count < m and idx <= num-1 and int_time[idx] <= check_bus[i]:
            last_crew = int_time[idx]
            count += 1
            idx += 1

                
        man_list.append(m - count)
    
    
    if i == len(check_bus) - 1:
        if man_list[i] != 0:
            return time_int_to_str(check_bus[i])
        else:
            return time_int_to_str(last_crew-1)