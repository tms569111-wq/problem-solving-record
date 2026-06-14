def solution(dartResult):
    # 스택적인 느낌적인 느낌
    stack=[]
    now_phase=-1
    for i in range(len(dartResult)):
        if dartResult[i-1]=='1' and dartResult[i]=='0':
            stack.pop()
            stack.append(10)
        elif dartResult[i].isdigit():
            stack.append(int(dartResult[i]))
            now_phase+=1
        elif dartResult[i]=='D':
            stack[now_phase]=stack[now_phase]**2
        elif dartResult[i]=='T':
            stack[now_phase]=stack[now_phase]**3
        elif dartResult[i]=='*':
            if now_phase!=0:
                stack[now_phase-1]=stack[now_phase-1]*2
                stack[now_phase]=stack[now_phase]*2
            else:
                stack[now_phase]=stack[now_phase]*2
        elif dartResult[i]=='#':
            stack[now_phase]=stack[now_phase]*(-1)
        print(stack,i)
    answer = sum(stack)
    return answer