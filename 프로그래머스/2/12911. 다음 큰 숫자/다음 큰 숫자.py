def solution(n):
    a=str(bin(n)).count('1')
    
    while n<1000000:
        n+=1
        z=bin(n)
        if str(z).count('1')==a:
            return int(z,2)
        