def solution(lines):
    # 선분이 나타날 수 있는 전체 범위 (-100 ~ 100)를 커버하는 리스트 생성
    # 각 인덱스는 '해당 지점부터 +1 구간'의 사용 횟수를 의미함
    count = [0] * 200 
    
    for start, end in lines:
        # 시작점부터 끝점 직전까지 1씩 더해줌 (구간을 채움)
        for i in range(start, end):
            count[i + 100] += 1 # 음수 인덱스 방지를 위해 100을 더함
            
    # 2개 이상의 선분이 지나간(값이 2 이상인) 칸의 개수를 합산
    answer = 0
    for c in count:
        if c >= 2:
            answer += 1
            
    return answer