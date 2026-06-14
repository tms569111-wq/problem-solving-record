def solution(routes):
    # 일단 겹치기
    # 겹치는 숫자가 생기면 인덱스랑 겹치는 숫자를 구해야 함
    # 어떻게? 감이 아예 안 오네...
    routes.sort(key=lambda x:x[1])
    last_camera=-30001
    answer=0
    for i in routes:
        # 한 대의 전체 루트
        if i[0]>last_camera:
            answer+=1
            last_camera=i[1]
            
    return answer