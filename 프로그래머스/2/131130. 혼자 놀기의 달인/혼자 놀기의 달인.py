def solution(cards):
    # 범위가 그렇게 넓지는 않다.
    # 이것은 링크드 리스트를 구현하는 문제 같다.
    # dic도 괜찮지만 리스트로 다음을 나타낼 수 있을까?
    # next[1] = 8이지만
    # next[2] = 6
    # 이거 굳이 그렇게 핧 필요 없나? 걍 for문으로 돌려가면서 check리스트에 있는지 아닌지 확인 하면 될 듯
    
    
    list_len = []
    check = [False] * len(cards)
    cards = [i - 1 for i in cards]
    
    for i in range(len(cards)):
        now = cards[i]
        if check[i] != True:
            check[i] = True
        elif check[i] == True:
            continue
        if now == i:
            list_len.append(1)
            continue
        num = 1
        while True:
            if check[now] != True:
                check[now] = True
            elif check[now] == True:
                list_len.append(num)
                break
            if cards[now] == now:
                list_len.append(num)
                break
            now = cards[now]
            num += 1
            
    list_len.sort()
    if len(list_len) < 2:
        return 0
    else:
        answer = list_len[-1] * list_len[-2]
        return answer