def solution(begin, end):
    # 약간 에라토스테네스의 체 느낌
    # 어떤 begin의 어떤 수가 2로 나누어 떨어지면
    # begin은 그 수
    # 3으로 나누어떨어지면 그 수
    # 4로 나누어 떨어져도 그 수
    # 쭉 쭉 해서 최소 약수가 그 수
    # 최소 약수 구하는 거 n정도 필요
    # 최악의 경우 5000 * n 임
    # 근데 n이 1억...;;;
    # n이 한 1만 정도면 아슬아슬하게 가능
    # 즉 logn정도
    # logn으로 약수 구하는 방법?
    # 에라토스테네스는 소수인지 아닌지만 판별
    # 만약 소수면 걍 1
    # 근데 소수 아닌 애들은?
    # 어차피 1부터 1만정도 까지만 n하면 되려나?
    # 아니지 소수인지도 결국 sqrt까지만 구하면 되지
    # 그러면 5000 * 1억을 sqrt하니까 1만
    # 5000만? 근데 연산 만으면 애매한데
    # 근데 더 줄일 수는 없을 것 같다....ㅠㅠ
    def sosu(n):
        
        if n == 1:
            return 0
        check = -1
        for i in range(2, int(n**0.5)+1): 
        
            if n % i == 0:
                
                if n//i > 10000000:
                    check = max(check, i)
                    continue
                else:
                    return n // i
        if check == -1:
            return 1
        else:
            return check
    answer = [sosu(num) for num in range(begin, end+1)]
            
    return answer