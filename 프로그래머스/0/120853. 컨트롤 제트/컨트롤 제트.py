def solution(s):
    list_z=[]
    list_z=s.split(' ')
    count=0
    temp=0
    for i in list_z:
        if i=='Z':
            count=count-temp
        else:
            count=count+int(i)
            temp=int(i)
    return count