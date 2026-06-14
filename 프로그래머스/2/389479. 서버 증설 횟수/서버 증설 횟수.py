def solution(players, m, k):
    # 중요한 건 총 숫자가 아닌 변화량
    # 서버가 1~2번 왔다갔다 해도 변화량 100만 뜰 수 있음
    # 일종의 누적합?
    # 단 변화량만 구하는 누적합
    now_server=0
    count=0
    check=[0]*50
    for hour in range(len(players)):
        now_server=check[hour]
        if players[hour]>=((now_server+1)*m):
            a=(players[hour]-(now_server*m))//m
            for j in range(k):
                check[hour+j]+=a
            count+=a
    return count