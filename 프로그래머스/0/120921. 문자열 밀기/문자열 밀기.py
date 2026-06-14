def solution(A, B):
    count=0
    i=len(A)
    while i>0:
        if A==B:
            return count
        A=A[-1]+A[0:len(A)-1]
        count+=1
        
        i=i-1
    answer = -1
    return answer