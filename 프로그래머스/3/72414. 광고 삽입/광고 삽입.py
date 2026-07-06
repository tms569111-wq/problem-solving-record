
def solution(play_time, adv_time, logs):
    # 일단 보니까 시간 많이 겹치기 구하는 포탄문제랑 비슷한데 
    # 포탄이 아니라 재생 시간까지 구해야 함
    # 이거는 각 구간이 많이 겹치는 녀석으로 구하면 안 됨
    # 만약 100천개가 10초 겹치고, 나머지 200천개가 1초 겹치면
    # 전자가 조금 겹치지만 더 많이 겹침
    # 만약 간단하게 생각해서 완전 탐색을 한다면...
    # 모든 logs의 시작 시간을 다 한 번 씩 해본다
    # 근데 이러면 30만번을 일단 연산 해야 하고
    # 각 연산에서 또 30만번 해야 하네...
    # 오 아닌가? 이거 리스트로 구하면
    # 일단 숫자로 변환하고 리스트에 2차원 배열로 싹다 구한 뒤
    # 둘다 오름차순으로 구하고
    # 맨 처음 원소 + adv_time으로 해서 구한 값이 정렬 된 리스트에 스타트보다 작기 전 까지 리스트들 구하고
    # adv_time을 구하면...
    # 와 근데 이건 너무 운에 맡기나. 만약 30만개인데 버틸 수 있는 건 300개 정도
    # 만약 겹치는 시간 구간이 너무 많으면 어려워질 듯
    # 사실상 nlogn문제인데 이게 쉽지 않네 뭐가 log n일 까...
    if play_time == adv_time:
        return '00:00:00'
    
    def time_to_int(time):
        h, m, s = time.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    
    def int_to_time(t):
        h = t // 3600
        t %= 3600
        m = t // 60
        s = t % 60
        return f"{h:02d}:{m:02d}:{s:02d}"
    
    adv = time_to_int(adv_time)
    play = time_to_int(play_time)
    time = [0] * (play + 2)
    max_time = 0
    answer = 0
    now = sum(time[:adv])
    
    for i in range(len(logs)):
        start, end = logs[i].split("-")
        time[time_to_int(start)] += 1
        time[time_to_int(end)] -= 1
    
    
    for i in range(1, play + 1):
        time[i] += time[i - 1]
        
    for start in range(1, play - adv + 1):
        now -= time[start - 1]
        now += time[start - 1 + adv]
        if now > max_time:
            max_time = now
            answer = start
    return int_to_time(answer)
    