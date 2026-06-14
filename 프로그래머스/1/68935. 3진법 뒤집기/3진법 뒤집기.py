def solution(n):
    st=''
    while (n//3!=0):
        st=st+str(n%3)
        n=n//3
        print(n)
    st=st+str(n%3)
    answer=0
    for i in range(len(st)):
        answer+=int(st[-1-i])*(3**i)
    return answer