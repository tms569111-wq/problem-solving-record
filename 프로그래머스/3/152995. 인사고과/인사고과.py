def solution(scores):
    # 완호 석차
    # 인센티브 못 받는 애들 체크
    # 일단 100000번이기 때문에 n^2이 되는 순간 망함
    # 먼저 완호 점수 저장 하고 합계 기준으로 sort하는 게 좋음
    # 이거 둘 다의 합보다 적은 기준이라면
    # 두 점수 사이의 차가 적은 순으로 정렬 후 비교 계산이 빠를 듯
    # 계산 빠르게 하려면 먼저 sort한 거에서 석차 부터 구하고
    # 각 석차를 비교
    # 이때 둘다 작아야 하니까 (최소한 자기보다 석차가 높은 놈들 혹은 합이 2보다 더 큰 놈들에게서 부터 체크 해야 함)
    # 완호 석차 구하고, 완호 앞에 있는 놈들 중에서 합계값이 2보다 크면서 각각의 크기가 2보다 큰 놈들 빼면 됨
    # 최악의 최악을 구하자면 완호가 꼴 등이고 앞에 모든 것들이 석차가 높은 경우
    # 일단 특별 조건 잘 모르겠으니까 해보자
    # 완호랑 점수 같으면 공동으로라서 걍 괜찮
    # 애초에 정렬할 때 둘 사이 차이의 절대값이 작은 놈들 기준
    answer = 0
    wanho = scores[0]
    wanho_sum = wanho[0] + wanho[1]
    
    scores.sort(key = lambda x: (-x[0], x[1]))
    
    max_second = -1
    
    rank = 1
    
    for first, second in scores:
        if second < max_second:
            if [first, second] == wanho:
                return -1
            continue
        max_second = max(max_second, second)
        
        if first + second > wanho_sum:
            rank += 1
    return rank