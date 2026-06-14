def solution(code):
    mode=0
    ret=''
    for i in range(len(code)):
        if code[i]=='1':
            if mode==0:
                mode=1
            else:
                mode=0
        else:
            if mode==0:
                if i%2==0:
                    ret=ret+code[i]
            else:
                if i%2==1:
                    ret=ret+code[i]
    if ret=='':
        return "EMPTY"
    else:
        return ret