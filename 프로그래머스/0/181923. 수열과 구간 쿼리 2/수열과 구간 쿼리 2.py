def solution(arr, queries):
    r=[]
    adf=1
    for h in range(0,len(queries)):
        temp=100000000
        s=queries[h][0]
        e=queries[h][1]
        k=queries[h][2]
        for i in range(s,e+1):
            if arr[i]>k:
                if arr[i]<temp:
                    temp=arr[i]

        if temp==100000000:
            r.append(-1)
        else:
            r.append(temp)
    return r