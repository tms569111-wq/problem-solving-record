def solution(numLog):
    z=''
    for i in range(len(numLog)):
        if i>0:
            if numLog[i]==numLog[i-1]+1:
                z=z+'w'
            elif numLog[i]==numLog[i-1]-1:
                z=z+'s'
            elif numLog[i]==numLog[i-1]+10:
                z=z+'d'
            else:
                z=z+'a'
    return z