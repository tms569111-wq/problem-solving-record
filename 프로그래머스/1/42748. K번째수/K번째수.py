def solution(array, commands):
    answer = []
    for z in commands:
        a=[]
        i,j,k=z[0],z[1],z[2]
        a=array[i-1:j]
        a.sort()
        answer.append(a[k-1])
    return answer