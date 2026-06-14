def solution(N, stations, w):
    now=1
    cover=2*w+1
    answer=0
    for station in stations:
        left=station-w
        right=station+w
        
        gap=left-now
        if gap>0:
            answer+=(gap+cover-1)//cover
        
        now=right+1
    if N>=now:
        gap=N-now+1
        answer+=(gap+cover-1)//cover  
    return answer