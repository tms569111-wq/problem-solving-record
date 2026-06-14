def solution(s):
    answer = ''
    check=0
    for i in range(len(s)):
        if s[i]==' ':
            answer+=' '
            check=-1
        elif check%2==0:
            answer+=s[i].upper()
        else:
            answer+=s[i].lower()
        check+=1
            
            
        
    return answer