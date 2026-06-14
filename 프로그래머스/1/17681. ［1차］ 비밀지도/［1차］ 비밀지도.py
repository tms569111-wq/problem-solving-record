def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a=arr1[i]|arr2[i]
        z=str(bin(a))[2:].zfill(n)
        b=''
        for j in z:
            if j=='1':
                b+='#'
            else:
                b+=' '
        print(b)
        answer.append(b)
    
    return answer