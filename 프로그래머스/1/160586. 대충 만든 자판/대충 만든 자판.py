def solution(keymap, targets):
    # 1. 알파벳별 최소 타수를 저장할 딕셔너리
    min_touch = {}
    
    # keymap을 돌며 각 문자의 가장 빠른 위치를 기록
    for key in keymap:
        for i, char in enumerate(key):
            # 처음 보는 문자거나, 기존보다 더 빨리 누를 수 있다면 업데이트
            if char not in min_touch or i + 1 < min_touch[char]:
                min_touch[char] = i + 1
    
    answer = []
    # 2. targets를 돌며 합계 계산
    for target in targets:
        total = 0
        for char in target:
            if char in min_touch:
                total += min_touch[char]
            else:
                # 만들 수 없는 문자가 하나라도 있으면 -1
                total = -1
                break
        answer.append(total)
        
    return answer
