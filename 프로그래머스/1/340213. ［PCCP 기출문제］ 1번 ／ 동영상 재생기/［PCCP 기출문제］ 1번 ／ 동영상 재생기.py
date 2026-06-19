from collections import deque
def str_to_int(s):
    a, b = s.split(":")
    return int(a)*60 + int(b)
def solution(video_len, pos, op_start, op_end, commands):
    q = deque(commands)
    now = str_to_int(pos)
    op_s = str_to_int(op_start)
    op_e = str_to_int(op_end)
    last = str_to_int(video_len)
    while q:
        if now < 0:
            now = 0
        if now >= last:
            now = last
        if op_s <= now and now <= op_e:
            now = op_e
        
        if q[0] == "next":
            now += 10
        elif q[0] == "prev":
            now -= 10
        q.popleft()
    if now < 0:
        now = 0
    if now >= last:
        now = last
    if op_s <= now and now <= op_e:
            now = op_e
    
    a = str(now//60)
    b = str(now - int(a)*60)
    if len(a) == 1:
        a = "0" + a
    if len(b) == 1:
        b = "0" + b
    answer = str(a + ":" + b)
    return answer