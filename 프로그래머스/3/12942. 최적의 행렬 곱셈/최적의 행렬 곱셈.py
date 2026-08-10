def solution(matrix_sizes):
    n = len(matrix_sizes)

    # dp[i][j]
    # i번째 행렬부터 j번째 행렬까지
    # 모두 곱하는 데 필요한 최소 연산 횟수
    dp = [[0] * n for _ in range(n)]

    # length = 현재 계산하려는 행렬 구간의 길이
    # 행렬 하나는 곱셈 비용이 0이므로 길이 2부터 시작
    for length in range(2, n + 1):

        # i = 구간 시작점
        for i in range(n - length + 1):

            # j = 구간 끝점
            j = i + length - 1

            dp[i][j] = float('inf')

            # i~j를 어디서 둘로 나눌 것인지 전부 확인
            for k in range(i, j):

                # i~k까지 만드는 비용
                left = dp[i][k]

                # k+1~j까지 만드는 비용
                right = dp[k + 1][j]

                # 두 결과 행렬을 마지막으로 곱하는 비용
                merge = (
                    matrix_sizes[i][0]
                    * matrix_sizes[k][1]
                    * matrix_sizes[j][1]
                )

                cost = left + right + merge

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]