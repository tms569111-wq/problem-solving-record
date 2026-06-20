def solution(picks, minerals):
    # 선택할 수 있는 것.
    # 다이아랑 철, 돌 곡갱이 중 1개 사용
    # 더 사용할 곡갱이가 없다는 거 보면 곡갱이가 없을 수도
    # 각 구간 별로 가장 빡센 것 다이아 5개면 다이아로
    # 그 다음 빡센 건 철로
    # 그 다음은 돌로 하기
    # 중요한 건 구간인데 5개 단위로 봐야 될 듯
    # 다행히 엄청 적은 숫자로 할 수 있으므로 완전탐색 하면 될듯???
    # 아니네 완탐하면 50!니까 너무 크다.
    # 구간별로 나누면 46번 정도만 하면 되나.
    # 일단 ㄱㄱㄱ
    # 야 근데 이거 애매하네
    # 5개씩 해서 제일 힘든 놈들을 보려면 놈들을 1, 5, 25로 변환 시키는 게 제일 좋을 듯
    answer = 0
    new_mine = []
    for i in minerals:
        if i == "diamond":
            new_mine.append(25)
        elif i == "iron":
            new_mine.append(5)
        else:
            new_mine.append(1)
    new_mine = new_mine[:sum(picks) * 5]
    for i in range(3):
        for j in range(picks[i]):
            max_num = 0
            max_idx = 0
            if len(new_mine) >= 5:
                for k in range(0,len(new_mine), 5):
                        
                    if max_num < sum(new_mine[k:k+5]):
                        max_num = sum(new_mine[k:k+5])
                        max_idx = k
                end_idx = min(max_idx + 5, len(new_mine))
                group = new_mine[max_idx : end_idx]
                if i == 0:
                    answer += len(group)
                elif i == 1:
                    for q in group:
                        if q == 1:
                            answer += 1
                        elif q == 5:
                            answer += 1
                        else:
                            answer += 5
                else:
                    answer += sum(group)
                new_mine = new_mine[0:max_idx] + new_mine[end_idx:]
            else:
                if i == 0:
                    answer += len(new_mine)
            
                elif i == 1:
                    for q in range(len(new_mine)):
                        if new_mine[q] == 1:
                            answer += 1
                        elif new_mine[q] == 5:
                            answer += 1
                        else:
                            answer += 5

                else:
                    answer += sum(new_mine)
                return answer
                    
                    
    return answer