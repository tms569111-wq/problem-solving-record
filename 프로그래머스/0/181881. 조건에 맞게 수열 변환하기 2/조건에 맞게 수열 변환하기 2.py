def solution(arr):
    answer = 0
    arr_1=[]
    while(arr_1!=arr):
        
        arr_1=arr[:]
        for i in range(len(arr)):
            if arr[i]>50 and arr[i]%2==0:
                arr[i]=arr[i]//2
            elif arr[i]<50 and arr[i]%2==1:
                arr[i]=arr[i]*2+1
        answer+=1
    
    return answer-1