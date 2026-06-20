def solution(enroll, referral, seller, amount):
    # 추천인과 등록자를 숫자로 변경하고
    # 숫자가 -1이 되거나 돈이 없을 때까지 while문 쓰면 쉽게 풀릴 듯한 느낌
    
    n = len(enroll)
    en_num = {}
    
    for i in range(n):
        en_num[enroll[i]] = i
    re_num = {}
    
    for i in range(n):
        if referral[i] != "-":
            re_num[enroll[i]] = en_num[referral[i]]
        else:
            re_num[enroll[i]] = -1
    
    result = [0] * n
    
    for money, sel in zip(amount, seller):

        money *= 100 
        while money > 0:
            count = money // 10
            result[en_num[sel]] += (money - count)
            parent_idx = re_num[sel]
            if parent_idx == -1:
                break
            sel = enroll[parent_idx]
            money = count
    return result
    
    