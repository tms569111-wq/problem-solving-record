def solution(emergency):
    # 1. 응급도가 높은 순서(내림차순)로 정렬된 리스트 생성
    sorted_list = sorted(emergency, reverse=True)
    
    # 2. 원본 리스트의 숫자가 sorted_list에서 몇 번째 인덱스인지 찾아 1을 더함
    return [sorted_list.index(i) + 1 for i in emergency]
