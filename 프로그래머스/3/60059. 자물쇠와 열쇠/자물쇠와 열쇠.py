def solution(key, lock):
    # 와 일단 막막하다.
    # 할 수 있는 것은 90도 회전 위아래 한 두칸
    # 20*20 = 400이니까
    # 400을 10만번 돌릴 수도 있으니까 경우의 수는 좀 많나
    # 단순 완전탐색하면 90도 시계로 돌리고 오른쪽 아래쪽 오른쪽 아래쪽 이런 식으로
    # 4개 중에 골라서 이거 나갈 때 까지인데
    # 일단 lock을 반전한 거(애초에 만들때 없는 걸 1로 만든 거랑)
    # key는 반전 안 한 거(애초에 만들 때 없는걸 0으로 만든 거)
    # key를 lock크기로 자른 부분이 같으면 정답
    # 아니면 x
    # 위, 아래, 왼쪽 오른쪽 모두 최대 20까지 가면
    # 전부 나가게 되서 의미 없음
    # 즉 dfs나 bfs로 4^20정도
    # 16 ^`10
    # 256 ^ 5
    # 50000*256 * 50000
    # 원래는 그런데 한 번 맨 처음 4개 중 한 곳 가면
    # 3개 중 한 곳 선택
    # 3^20인가?
    # 아니 근데 시계방향, 반 시계 방향도 고려해야 함.
    # 90도 회전 이니까 모든 경우의 수에 4를 곱해야 함
    # 3^20도 아니지. 위로 일단 한 칸 가고, 오른쪽 한 칸 가면 다시 왼쪽이나 위칸 못 가지
    # 무조건 오른쪽 위쪽 오른쪽 위쪽 이렇게만 가능
    # 오히려 2중 for문을 쓰면 간단하군
    # 이동을 원래 크기에서 [i][j]가 있다고 하면 전체 i랑 j를 
    # -20~+20 j도 -~20부터 +20까지
    # 1600번 3600 * 4 14400
    # 2000만번으로 되긴 하네
    # 이게 정답인듯?
    # 근데 이거 터질 수도
    # 상수항 생각하면...
    # 일단 해봐?
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 1:
                lock[i][j] = 0
            else:
                lock[i][j] = 1
    for _ in range(4):
        key = [list(row) for row in zip(*key[::-1])]
        for i in range(-len(key) - 1, len(lock), 1):
            for j in range(-len(key) - 1, len(lock), 1):
                new = [[0 for _ in range(len(lock))] for _ in range(len(lock))]
                for k in range(0, len(key)):
                    for q in range(0, len(key)):
                        if (k + i) >= 0 and (k + i) <= len(lock) -1 and (q + j) >= 0 and (q + j) <= len(lock) - 1: 
                            new[k + i][q + j] = key[k][q]
                if new == lock:
                    return True
    
    answer = False
    return answer