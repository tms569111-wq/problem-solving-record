def solution(s, skip, index):
    answer = ''
    for i in s:
        a=i
        count=0
        while count!=index:
            a=chr(ord(a)+1)
            if a in skip:
                continue
            elif ord(a)>ord('z'):
                a=chr(ord(a)-26)
                if a in skip:
                    continue
            count+=1
        answer+=a
    
    return answer