def solution(arr):
    answer=[0,0]
    def quad(x,y,size):
        half=size//2
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[x][y]!=arr[i][j]:
                    quad(x,y,half)
                    quad(x+half,y,half)
                    quad(x,y+half,half)
                    quad(x+half,y+half,half)
                    return
        answer[arr[x][y]]+=1
    quad(0,0,len(arr))
    return answer