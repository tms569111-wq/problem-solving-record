def solution(n, words):
    check=1
    already=[]
    already.append(words[0])
    for i in range(1,len(words)):
        print("i",i)
        print("word",words[i])
        print("i%n",i%n)
        
        if i%n==0:
            check+=1
        print("check",check)
        if words[i-1][-1]!=words[i][0]:
            return [(i)%(n)+1,check]
        if words[i] in already:
            return [i%n+1,check]
        already.append(words[i])
    print(already)
    return [0,0]