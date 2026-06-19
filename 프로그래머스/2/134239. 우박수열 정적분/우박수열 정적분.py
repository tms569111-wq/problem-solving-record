def solution(k, ranges):
    # 콜라츠 추측 이용해서 일단 1까지 만들기
    # 정적분 넓이는 1칸 기준 1 * 작은 y + 큰 (y -작은 y)/2*1(삼각형과 사각형 즉 사다리꼴)
    # 사다리꼴이니까 긴 거 + 작은 거 /2*1러 헤더 되는 구나
    # 시간 초과 체크 (k를콜라츠 추측하고 넓이를 구할 때 10000에 콜라츠 추측 하면 그래도 100만은 안 될 듯, 넓이 해도 ㄱㅊ)
    # b는 200단위, 10000개 해도 200만정도라 시간 over되진 않네.
    # 좋아. 해보자.
    answer = []
    # 1단 콜라츠
    colla_n = []
    def collatz(k):
        colla_n.append(k)
        while k != 1:
            if k % 2 == 0:
                k = k // 2
            else:
                k = k * 3 + 1
            colla_n.append(k)
        return
    area = []
    # 2젠 넓이 행렬 만들기
    def area_all(col):
        for i in range(len(col)-1):
            a = float(0.0) 
            a = (float(col[i]) + float(col[i+1]))/2
            area.append(round(a, 1))
        
    collatz(k)
    area_all(colla_n)
    length = len(colla_n)

    for start, last in ranges:
        new_last = length + last -1
        if new_last < start:
            answer.append(-1)
        else:
            answer.append(sum(area[start:new_last]))  
        
    return answer