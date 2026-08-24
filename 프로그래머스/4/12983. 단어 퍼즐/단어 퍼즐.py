# 긴거 순서대로 채우기
# 20000 * 100개이므로
# 최대 200만
# 근데 긴 단어가 안 좋을 수도? 긴단어 + 짧은 단어 여러 개가 오히려 짧은 단어 조금 많이 보다도 구릴 수도...
# 흠....아닌가?
# 각 단어 담아서 큰 단어 순으로 단어 뭉탱이로 자르면 될 것 같긴 한데...
def solution(strs, t):
    word_set = set(strs)
    INF = 20001
    dp = [INF] * (len(t) + 1)
    dp[0] = 0
    for end in range(1, len(t) + 1):
        for length in range(1, 6):
            start = end - length
            if start < 0:
                    break
            if dp[start] == INF:
                continue
            if t[start:end] in word_set:
                dp[end] = min(dp[end], dp[start] + 1)
    return dp[-1] if dp[-1] != INF else -1