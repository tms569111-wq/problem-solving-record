# 일단 길이 자체는 얼마 안 됨
# 근데 동전을 몇 번 뒤집어야 되는지 대충 막 뒤집다가 안 되네 할 수는 없음
# 가능한 경우와 불가능한 경우를 판단해야 됨
# 근데 그걸 어떻게 판단하지?
# 가능만 하다면야 dp로 노가다 하면 쉽게 구해짐
# 시간 복잡도가 어떤 걸 뒤집는 다면 그 뒤집힌 상태에서 다시 뒤집을 수 있으니까
# 자기 원래 뒤집었던 거 빼면 19개씩 늘어남. 19 * 19 * 19 반복
# 근데 불가능한 걸 가능하다고 생각하고 무한 반복하면 타임 오버
# 뭐 100만번 넘어가면 힘들어서 못 만든다고 할 수도 있겠지만
# 100만 1번 째에 될 수도 있으니까...
# 일단 dp부터 할까.
def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    
    diff = [
        [
            beginning[i][j] ^ target[i][j]
            for j in range(m)
        ]
        for i in range(n)
    ]
    answer = float('inf')
    for first_row_flip in [0, 1]:
        row_flip = [0] * n
        col_flip = [0] * m
        
        row_flip[0] = first_row_flip
        
        for j in range(m):
            col_flip[j] = diff[0][j] ^ row_flip[0]
        for i in range(n):
            row_flip[i] = diff[i][0] ^ col_flip[0]
        
        possible =True
        for i in range(n):
            for j in range(m):
                actual_flip = row_flip[i] ^ col_flip[j]
                
                if actual_flip != diff[i][j]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            flip_count = sum(row_flip) + sum(col_flip)
            answer = min(answer, flip_count)
    if answer == float('inf'):
        return -1
    return answer
        