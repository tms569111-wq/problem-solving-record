def solution(brown, yellow):
    wh=brown+yellow
    for i in range(1, int(wh**0.5)+10):
        if wh%i==0:
            if (i-2)*(int(wh//i)-2)==yellow:
                return [max(i,int(wh//i)),min(i,int(wh//i))]
    return [4,3]