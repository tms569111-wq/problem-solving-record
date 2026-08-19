# 이거는 그리디 느낌이지만?
# 만약 경우의 수가 여러개 있는데 그중 다른 수를 선택해서 변하는가...
# 즉 현재 있는 것들 중 2개를 버리는데 이때 조합 자체는 그리디가 되는 게 어차피 2개니까
# 값이 정해져 있음 근데 경우의 수를 살펴 보자면
# 다음 라운드로 가기 위한 카드가 없을 때
# 다음 2개 카드 중 coin을 써서 카드를 얻어서 넘어갈 수 있다면
# 무조건 넘어감
# 그러나 안 먹어도 넘어갈 수 있는데
# 굳이 coin으로 먹어야 되는가?
# 이건 신의 한수가 될 지 안 될지는 뒤로 가봐야만 알 수가 있음.
# 그러나!
# 역발상으로 거꾸로 생각해서 맨 뒤 최대 라운드부터 내려오면서
# 현재 카드로 몇 라운드까지 올 수 있나?
# 이걸 따져보는 게 오히려 맞지 않나...
# coin으로 전부 먹기, 전부 안 먹기, 각각 1개씩 먹기로 경우의 수가 4개씩 4 ^ 1000하는 것 보다는
# 맨 뒤 부터 되나 안 되나 따질 까 싶은데...
# 사실 이것도 아니네. 맨 뒤는 코인 무한정이면 무조건 되는 구나.
# 1라운드부터 뒤에 있는 카드 조합으로 해결이 되는 가? 이게 되면
# 2라운드부터 뒤에 있는 카드 조합으로 해결이 되는가?
# ....
# n라운드부터 뒤에 있는 카드 조합으로 해결이 되는가?
# 만약 이것들이 될 때 맨처음 시작하고 있는 수를 제외한 다른 수를 사용하려면
# coin을 써야 함.
# 즉 n라운드에서 뒤에 있는 카드 조합이 n개 이상이 안 되면 무조건 탈락
# n개 이상이어도 맨처음 무료로 주는 카드가 아니라면 coin을 소모하되 coin을 다 썼다면 무조건 탈락
# 혹은 끝 라운드까지 도달하거나 하면 종료임
# 좋아 한 번 짜볼까?
def solution(coin, cards):
    n = len(cards)
    goal = n + 1

    hand = set(cards[:n // 3])
    drawn = set()

    idx = n // 3
    round_count = 1

    while idx < n:
        drawn.add(cards[idx])
        drawn.add(cards[idx + 1])
        idx += 2

        found = False

        for card in list(hand):
            pair = goal - card

            if pair in hand:
                hand.remove(card)
                hand.remove(pair)

                found = True
                break

        if found:
            round_count += 1
            continue

        if coin >= 1:
            for card in list(hand):
                pair = goal - card

                if pair in drawn:
                    hand.remove(card)
                    drawn.remove(pair)

                    coin -= 1
                    found = True
                    break

        if found:
            round_count += 1
            continue

        if coin >= 2:
            for card in list(drawn):
                pair = goal - card

                if pair in drawn:
                    drawn.remove(card)
                    drawn.remove(pair)

                    coin -= 2
                    found = True
                    break

        if found:
            round_count += 1
            continue

        break

    return round_count