def solution(s):
    n = len(s)

    # 긴 길이부터 검사
    for length in range(n, 0, -1):
        for start in range(0, n - length + 1):
            end = start + length - 1

            left = start
            right = end
            is_palindrome = True

            while left < right:
                if s[left] != s[right]:
                    is_palindrome = False
                    break

                left += 1
                right -= 1

            if is_palindrome:
                return length