def solution(number, n, m):
    if number%n==0:
        if number%m==0:
            return 1
        else:
            return 0
    else:
        return 0