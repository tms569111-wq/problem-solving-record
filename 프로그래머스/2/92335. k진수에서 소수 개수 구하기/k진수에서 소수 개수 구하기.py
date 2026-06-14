def solution(n, k):
    word=""
    while n>0:
        word = str(n % k) + word
        n=n//k
    count=0
    a=word.split('0')
    print(a)
    for i in a:
        
        if i=='' or i=='1':
            continue
        w=int(i)
        check=0
        for j in range(2,int(w**0.5)+1):
            if w%j==0:
                check=1
                break
        if check==0:
            count+=1
    return count