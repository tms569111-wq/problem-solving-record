def solution(s):
    answer = 0
    stack=[]
    check_left=['(','[','{']
    check_right=[')',']','}']
    for k in range(len(s)):
        s=s[1:len(s)]+s[0]
        for i in range(len(s)):
            if stack==[] or i==0:
                stack.append(s[i])
            else:
                check=0
                for j in range(3):
                    if stack[-1]==check_left[j]:
                        if s[i]==check_right[j]:
                            stack.pop()
                            check=1
                            break
                if check==0:
                    stack.append(s[i]) 
        if stack==[]:
            answer+=1
        stack=[]
    
    return answer