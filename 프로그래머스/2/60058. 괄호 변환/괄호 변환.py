def solution(p):
    # 누가봐도 스택적인 느
    
    fa = ''
    

    
    def right(u):
        stack = []
        for i in u:
            if i == "(":
                    stack.append(i)
            elif i == ")":
                if stack != [] and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        if stack == []:
            return True
        else:
            return False
    
    def check(p):
        answer = ''
        if p == '':
            return ''
        if right(p) == True:
            return p
        else:
            u = ''
            v = ''
            check_open = 0
            check_close = 0
            for i in range(len(p)):
                if p[i] =="(":
                    check_open += 1
                elif p[i] ==")":
                    check_close += 1
                if  check_open != 0 and check_open == check_close:
                    u = p[:i+1]
                    v = p[i+1:]
                    break
            if right(u) == True:
                answer += u
                answer += check(v)
                return answer
            else:
                
                new = '('
                u = u[1:-1]
                v = check(v)
                new += v
                new += ')'
                q = ''
                for i in u:
                    if i == "(":
                        q += ")"
                    else:
                        q += "("
                new += q
                return new
                
                
                
    fa = check(p)
    return fa
    