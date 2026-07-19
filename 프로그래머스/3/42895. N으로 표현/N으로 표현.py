# N은 1 부터 9이하
# N으로 number을 사칙연산으로 구해야 함
# 9가 있다고 했을 때 9로 할 수 있는 사칙연산 곱하기 나누기(나머지 무시) 더하기 빼기
# 괄호 사용 가능
# 만들 수 있는 수의 개수는?
# 9+9 + 9/ 9 = 3 ~ 이런식으로 1부터 n까지 다 가능함
# 즉 number의 수가 크면 클 수록 9가 유리
# 그러나 9보다 작을 때는 다름
# 근데 또 999같은건 되네
# 일단...dp인 건 number을 만들 수 있는 최소값을 저장하라는 뜻인 건 이해 완료
# dp[222] = 2 2 2 해서 222
# 흠...난이도 높네 뭘 어찌해야 하나
# 모르겠다 감도 안 옴
def solution(N, number):
    if N == number:
        return 1
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for left in dp[j]:
                for right in dp[i - j]:
                    dp[i].add(left + right)
                    dp[i].add(left - right)
                    dp[i].add(left * right)
                    if right != 0:
                        dp[i].add(left // right)
        if number in dp[i]:
            return i
    return -1