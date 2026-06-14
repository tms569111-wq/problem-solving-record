def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = {x: nums.count(x) for x in set(nums)}
    unique_nums = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    
    # 1. 네 숫자가 모두 같은 경우
    if len(counts) == 1:
        p = unique_nums[0]
        return 1111 * p
    
    # 2. 세 숫자가 같고 하나가 다른 경우 (p가 3개, q가 1개)
    elif len(counts) == 2 and counts[unique_nums[0]] == 3:
        p, q = unique_nums[0], unique_nums[1]
        return (10 * p + q) ** 2
    
    # 3. 두 개씩 같은 값이 나오는 경우 (p가 2개, q가 2개)
    elif len(counts) == 2 and counts[unique_nums[0]] == 2:
        p, q = unique_nums[0], unique_nums[1]
        return (p + q) * abs(p - q)
    
    # 4. 두 개만 같고 나머지 두 개는 각각 다른 경우 (p가 2개, q, r이 각각 1개)
    elif len(counts) == 3:
        p = unique_nums[0] # 빈도가 2인 숫자
        q, r = unique_nums[1], unique_nums[2]
        return q * r
    
    # 5. 네 숫자가 모두 다른 경우
    else:
        return min(nums)