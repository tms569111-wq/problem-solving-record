def solution(s):
    stack=[]
    
    for char in s:
        if stack!=[] and stack[-1]==char:
            stack.pop()
        else:
            stack.append(char)

    if stack==[]:
        return 1
    else:
        return 0