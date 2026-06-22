def solution(s):
    # len(s) //2 보다 더 커지면 의미가 없음
    # 시간복잡도로 보면 1000 * 1000 100만 정도인가
    # 앞 뒤로 i 크기만큼 잘라서 비교해서
    # 만약 같으면 num+=1
    # str(num) + last
    answer = len(s)
    
    for unit in range(1, len(s)//2 + 1):
        compressed = ""
        
        prev = s[0:unit]
        count =1 
        for i in range(unit, len(s), unit):
            cur = s[i:i+unit]
            if cur == prev:
                count += 1
            else:
                if count == 1:
                    compressed += prev
                else:
                    compressed += str(count) + prev
                prev = cur
                count = 1
        
        if count ==1:
            compressed += prev
        else:
            compressed += str(count) + prev
        answer = min(answer, len(compressed))
    return answer
   