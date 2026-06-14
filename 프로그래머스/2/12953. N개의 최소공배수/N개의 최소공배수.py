import math
def solution(arr):
    a=1
    q=len(arr)
    i=0
    while i<q-1: 
        z=arr[i]*arr[i+1]//math.gcd(arr[i],arr[i+1])
        a=a*z//math.gcd(a,z)
        i+=1
    answer = a
    
    return answer