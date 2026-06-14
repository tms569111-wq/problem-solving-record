def solution(arr):
    check=0
    position=0
    length=100000
    answer = []
    for i in range(len(arr)):
        if arr[i]==2 and check==0:
            check=1
            position=i
        elif arr[i]==2 and check==1:
            length=i-position
            answer=answer+arr[position:i+1]
            position=i
            check=2
        elif arr[i]==2 and check==2:
            length=i-position
            answer=answer+arr[position+1:i+1]
            position=i
                
    if check==1 and answer==[]:
        return [2]
    elif check==0 and answer==[]:
        return [-1]
    return answer