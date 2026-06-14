import math
def solution(progresses, speeds):
    a=[]
    for i in range(len(progresses)):
        a.append(math.ceil((100-progresses[i])/speeds[i]))
    target=a[0]
    que=[]
    count=0
    for j in range(len(a)):
        if a[j]<=target:
            count+=1
        else:
            que.append(count)
            count=1
            target=a[j]
    if count!=0:
        que.append(count)
    return que
        