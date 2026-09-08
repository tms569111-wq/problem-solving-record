from collections import defaultdict
def check(u):
    stack = []
    for i in range(len(u)):
        if u[i] == '(':
            stack.append('(')
        elif u[i] == ')':
            if stack == []:
                return False
            else:
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
    return True
def solution(p):
    answer = ''
    if p == '':
        return ''
    dic = defaultdict(int)
    now = ''
    for i in range(len(p)):
        if p[i] == '(':
            dic['('] += 1
        elif p[i] == ')':
            dic[')'] += 1
        if dic['('] == dic[')']:
            u = p[0:i + 1] 
            v = p[i + 1:]
            break
    if check(u):
        answer += u + solution(v)
    else:
        u = u[1:-1]
        new_u = ''
        for i in u:
            if i == '(':
                new_u += ')'
            else:
                new_u += '('
        answer += '(' + solution(v) + ')' + new_u
    return answer
    