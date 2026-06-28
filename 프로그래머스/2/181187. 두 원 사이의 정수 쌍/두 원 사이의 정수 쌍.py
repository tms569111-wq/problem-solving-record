import math
def solution(r1, r2):
    # 어떤 정수 좌표 값 x, y 제곱 더한 값이 r1 **2 보다는 크고 r2*2보다는 작아야 되는데
    # 이게 200만 * 200만 개 세버리면 에바세바
    # x = 0부터 ~~~ y = 0직전까지
    # 4개분면 원이라 같으니까 곱하기 4하면 딤
    # 그래도 100만 * 100만
    # 일단 시작은 r2 - r1부터
    # y는 1씩 올리는데 이때 최적화가 필요 할 듯?
    # 일단 4분면 싹다 하는 거 부터 계산
    r2_d = r2 ** 2
    r1_d = r1 ** 2
    answer = 0
    
    # r1 **2 - 1**2부터 r1**2 -1**2 까지
    for i in range(1, r2 + 1, 1):
        if i >= r1:
            answer += math.floor(math.sqrt(r2_d - i**2)) + 1
        else:
            answer += math.floor(math.sqrt(r2_d - i**2)) - math.ceil(math.sqrt(r1_d - i**2)) + 1
        
    return answer * 4