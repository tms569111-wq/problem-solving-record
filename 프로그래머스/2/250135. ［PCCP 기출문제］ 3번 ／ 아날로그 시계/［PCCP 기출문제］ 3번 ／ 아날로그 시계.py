def solution(h1, m1, s1, h2, m2, s2):
    TOTAL = 60 * 60 * 12
    # h1 = 1초에 total + 1만큼 감
    # m1 =  1초에 total + 12
    # s1 = 1초에 720
    # 각 것들은 끝까지 오면 컴백함
    # 단 이때 1초 단위가 아니라 아주 세세한 초 단위이기 때문에
    # 0.0001초에서 겹쳐도 겹쳐짐
    # 10만 이하로 지나면 괜찮.
    # 몇 . 몇몇몇 초에 어디인지 안 나타나기 때문에
    # 그냥 앞 뒤인지만 체크 하면 될 듯
    def time_to_int(h, m, s):
        return h * 3600 + m * 60 + s
    start = time_to_int(h1, m1, s1)
    end = time_to_int(h2, m2, s2)
    def count(t):
        minute = t * 59 // 3600
        hour = t * 719 // 43200
        
        duplicate = t // 43200
        return minute + hour - duplicate
    answer = count(end) - count(start)
        
    if start % 3600 == 0:
        answer += 1
    return answer