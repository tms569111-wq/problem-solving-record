from itertools import permutations

def solution(expression):
    operand_list = ["+", "-", "*"]
    def cal(a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
    def token(ex):
        arr = []
        num = ''
        for i in ex:
            if i.isdigit():
                num += i
            else:
                arr.append(int(num))
                arr.append(i)
                num = ''
        arr.append(int(num))
        return arr
    tok = token(expression)
    answer = 0
    for i in permutations(operand_list):
        new = tok[:]
        for op in i:
            
            stack = []
            stack.append(new[0])
            for v in range(1, len(new), 2):
                operand = new[v]
                number = new[v+1]
                if operand == op:
                    a = stack.pop()
                    stack.append(cal(int(a), int(number), operand))
                else:
                    stack.append(operand)
                    stack.append(number)
                
            new = stack
        
        answer = max(answer, abs(new[0]))
    return answer
