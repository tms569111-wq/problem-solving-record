# 시간이 겁나 많이 걸릴 것 같기 때문에 이분 탐색 사용

def solution(diffs, times, limit):
    right = max(diffs)
    left = 1
    while left<=right:
        time = 0
        mid = (left + right)//2
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                time += times[i]
            else:
                time += times[i] + (times[i-1] + times[i]) * (diffs[i] - mid)
        if time > limit:
            left = mid + 1
        if time <= limit:
            right = mid - 1

    return left
        
        
                
    answer = 0
    return answer