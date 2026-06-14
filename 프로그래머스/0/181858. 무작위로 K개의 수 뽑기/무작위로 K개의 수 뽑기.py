def solution(arr, k):
    answer = []
    
    # 1. arr의 요소를 직접 하나씩 꺼내면 인덱스 초과 오류가 나지 않습니다.
    for num in arr:
        # 이미 들어있는 숫자인지 확인하고, 아직 k개를 다 안 채웠다면 추가
        if num not in answer:
            answer.append(num)
        
        # k개를 모두 채웠다면 더 이상 검사할 필요 없이 반복문을 종료합니다.
        if len(answer) == k:
            break
            
    # 2. 반복문이 끝났는데 k개보다 부족하다면 -1을 채워줍니다.
    while len(answer) < k:
        answer.append(-1)
            
    return answer
