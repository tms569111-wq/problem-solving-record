from collections import defaultdict
def solution(friends, gifts):
    # 준 횟수와 받은 횟수
    # 이거 gifts와 friends가 곱해도 50만 밖에 안 됨
    # 굉장히 여유로움
    # 먼저 dic에서 해시로 승부봐야 함
    # dic에다가 []로 넣기
    # 이때 dic에서 각 친구에 대한 선물 크기를 매번 갱신해도 50 그래봤자 50이라 널널
    # 바로 시작
    # 먼저 준 횟수
    # 이것도 그냥 해시로
    give_num = defaultdict(int)
    take_num = defaultdict(int)
    who = defaultdict(dict)
    for i in range(len(gifts)):
        giver, taker = gifts[i].split()
        give_num[giver] += 1
        take_num[taker] += 1
        if taker in who[giver]:
            who[giver][taker] += 1
        else:
            who[giver][taker] = 1
    answer = 0
    for i in range(len(friends)):
        check_i = 0
        for j in range(len(friends)):
            if i != j:
                if friends[j] in who[friends[i]]:
                    if friends[i] not in who[friends[j]]:
                        check_i += 1
                    else:
                        if who[friends[i]][friends[j]] > who[friends[j]][friends[i]]:
                            check_i += 1
                        elif who[friends[i]][friends[j]] == who[friends[j]][friends[i]]:
                            if give_num[friends[i]] - take_num[friends[i]] > give_num[friends[j]] - take_num[friends[j]]:
                                check_i += 1
                            
                else:
                    if friends[i] in who[friends[j]]:
                        continue
                    elif give_num[friends[i]] - take_num[friends[i]] > give_num[friends[j]] - take_num[friends[j]]:
                        check_i += 1
                                          
                        
        answer = max(answer, check_i) 
    
    return answer