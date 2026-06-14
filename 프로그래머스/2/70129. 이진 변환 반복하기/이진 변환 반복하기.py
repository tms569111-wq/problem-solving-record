def solution(s):
    count=0
    check=0
    while True:
        print(s)
        a=s.count('0')
        s=bin(len(s)-a)
        s=s[2:]
        count+=a
        if a==0 and len(s)==1:
            break
        check+=1
    answer = [check,count]
    return answer