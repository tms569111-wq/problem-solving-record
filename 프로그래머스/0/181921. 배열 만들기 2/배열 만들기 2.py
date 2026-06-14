def solution(l, r):
    z=''
    k=''
    temp=''
    zz=[]
    for i in range(l,r+1):
        z=str(i)
        z=z.replace("0", "")
        z=z.replace("5", "")
        if z=='':
            zz.append(i)
    if zz==[]:
        zz.append(-1)
    return zz