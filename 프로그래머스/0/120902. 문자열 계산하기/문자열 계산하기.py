def solution(my_string):
    a=[]
    count=0
    a=my_string.split()
    for i in range(0,len(a)-1,2):
        print(i)
        if i==0:
            count=int(a[0])
        if a[i+1]=='+':
            count=count+int(a[i+2])
        else:
            count=count-int(a[i+2])
            
    return count
