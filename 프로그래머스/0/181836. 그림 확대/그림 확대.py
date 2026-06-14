def solution(picture, k):
    arr=[]
    for i in range(len(picture)):
        new=''
        for j in range(len(picture[i])):
            new=new+picture[i][j]*k
        
        for z in range(k):
            arr.append(new)
        

    
    return arr