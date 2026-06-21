def solution(n, money):
    # 이거 자체는 그리드 알고리즘 느낌
    # 탐욕법 쓰기에는 근데 정답이 너무 커질 수 있다고 함
    # 이런 경우는 무조건 dp일 확률이 높음
    # 근데 이건 어떻게 dp로 하는가?
    # 특정 dp[0~n]까지 두고 특정 n원에서 바로?
    # 아니면 dp[0]에서 하고 dp[1]은 dp[0]에서 dp[1]로 갈 수 있는 경우에 수인가?
    # 근데 money가 다를 텐데
    # dp[2] + dp[3] = dp[5]가 되지 않음...
    # 왜냐하면 money가 다르기 때문
    # 감도 안 오네 일단 완전탐색으로 해두고 dp로 바꿔보도록 하자
    
    MOD = 1000000007
    dp = [0] * (n+1)
    dp[0] = 1
    for coin in money:
        for price in range(coin, n+1):
            dp[price]  = (dp[price] + dp[price - coin]) % MOD
    return dp[n]
        
    
    return answer