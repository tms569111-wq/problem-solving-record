def solution(money):
    # DP라는 큰 힌트가 주어졌다.
    # 매우 짧은 문제
    # 인접한 두 집을 털면 망함
    # 즉 이전 집을 더할 수 없음
    # 그리고 원형이기 때문에 끝 집은 현재 집을 추가해야 함
    pre_money = money[1:]
    dp_pre = [0] * (len(money) + 1)
    dp_pre[0] = pre_money[0]
    dp_pre[1] = max(pre_money[0], pre_money[1])
    
    for i in range(2, len(pre_money)):
        dp_pre[i] = max(pre_money[i] + dp_pre[i-2], dp_pre[i-1])
    
    front_money = money[:-1]
    dp_front = [0] * (len(money) + 1)
    dp_front[0] = front_money[0]
    dp_front[1] = max(front_money[0], front_money[1])
    
    
    for i in range(2, len(front_money)):
        dp_front[i] = max(front_money[i] + dp_front[i-2], dp_front[i-1])

    
    answer = max(max(dp_pre), max(dp_front))
    
    return answer