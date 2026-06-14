def solution(order):
    answer=0
    stack=[]
    now_num=1
    for i in order:
        while now_num<=i:
            stack.append(now_num)
            now_num+=1

        if stack!=[] and stack[-1]==i:
            stack.pop()
            answer+=1
            
        else:
            break
            
    
    return answer