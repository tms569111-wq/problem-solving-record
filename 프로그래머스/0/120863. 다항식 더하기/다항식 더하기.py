def solution(polynomial):
    x_1=0
    x_0=0
    a=[]
    a=polynomial.split()
    for i in a:
        if 'x' in i:
            if i[0]=='x':
                x_1+=1
            else:
                i=i.replace('x','')
                
                x_1+=int(i)
                print(i)
        elif 'x' not in i and '+' not in i:
            x_0+=int(i)
    if x_1==0:
        if x_0==0:
            return ''
        else:
            return str(x_0)
    elif x_0==0:
        if x_1!=0:
            if x_1==1:
                return 'x'
            else:
                return str(x_1)+'x'
    if x_1==1:
        answer='x + '+str(x_0)
    else:
        answer = str(x_1)+'x + '+str(x_0)
    return answer