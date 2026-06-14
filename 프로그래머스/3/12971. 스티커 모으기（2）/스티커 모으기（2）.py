def solution(sticker):
    # dp로 푸는 문제인 듯 하구먼...
    answer = 0
    n=len(sticker)
    if len(sticker)==1:
        return sticker[0]
    def want_dp(arr):
        if len(arr)==1:
            return arr[0]
        elif len(arr)==2:
            return max(arr[0],arr[1])
        dp=[0]*n
        dp[0]=arr[0]
        dp[1]=max(dp[0],arr[1])
        for i in range(2,len(arr)):
            dp[i]=max(dp[i-1],dp[i-2]+arr[i])
        return dp[i]
    answer=max(want_dp(sticker[0:-1]),want_dp(sticker[1:]))
    return answer