def solution(n, t, m, p):
    # n진법으로 짜르고 짜른 숫자를 하나 하나 queue리스트에 넣어야 함.
    # 10진법 넘으면 [A,B,C,D,E,F]
    # 넣은 리스트의 len을 m으로 나눔. n번 해야 하면 p를 0~m번 까지 곱한 리스트를 출력
    def convert(num,base):
        digits="0123456789ABCDEF"
        if num==0:
            return "0"
        result=""
        while num>0:
            result=digits[num%n]+result
            num//=n
        return result
    
    
    
    full_string=""
    current_num=0
    while len(full_string)<t*m:
        full_string+=convert(current_num,n)
        current_num+=1
    answer=full_string[p-1:t*m:m]
        
    
    return answer[:t]
    