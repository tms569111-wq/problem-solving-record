def solution(a, b, n):
    result = 0
    while n >= a:
        new_coke = (n // a) * b
        result += new_coke
        n = (n % a) + new_coke
        
    return result
