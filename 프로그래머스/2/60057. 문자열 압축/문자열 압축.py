def solution(s):
    n = len(s)
    answer = 1e19
    if n <= 2:
        return n
    for i in range(1, n // 2 + 1):
        previous = s[:i]
        pre_count = 1
        now = ""
        for j in range(i, n, i):
            new = s[j:i + j]
            if new != previous:
                if pre_count >= 2:
                    now += str(pre_count)
                now += previous
                previous = new
                pre_count = 1
            else:
                pre_count += 1
            
        if pre_count >= 2:
            now += str(pre_count)

        now += previous
        answer = min(len(now), answer)
    return answer