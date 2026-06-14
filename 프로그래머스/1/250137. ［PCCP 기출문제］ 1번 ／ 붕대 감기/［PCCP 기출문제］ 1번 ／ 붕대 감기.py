def solution(bandage, health, attacks):
    # 일단 공격 시간...for문으로 체크
    # health가 최대이면 now_health가 더 못 올라가게 체크
    # 시간은 now_time으로 체크
    # 파이썬은 리스트 조회할 때 인덱스로 조회하면 시간복잡도가 1이므로
    # now_time으로 시간 가는 걸 체크하고, 인덱스로 조회하기
    last_time=attacks[-1][0]
    combo=0
    now_health=health
    attacks_idx=0
    last=len(attacks)
    for now_time in range(1, last_time+1):
        if attacks[attacks_idx][0]==now_time:
            now_health-=attacks[attacks_idx][1]
            attacks_idx+=1
            combo=0
            if now_health<=0:
                return -1
            if attacks_idx==last:
                return now_health
        elif now_time!=0:
            combo+=1
            if combo==bandage[0]:
                now_health+=bandage[1]
                now_health+=bandage[2]
                if now_health>=health:
                    now_health=health
                combo=0
            else:
                now_health+=bandage[1]
                if now_health>=health:
                    now_health=health
                
    return -1