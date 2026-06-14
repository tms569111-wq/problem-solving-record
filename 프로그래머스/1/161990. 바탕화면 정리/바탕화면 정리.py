def solution(wallpaper):
    # 가장 왼쪽, 가장 오른쪽, 가장 높이, 가장 낮게
    i_list=[]
    j_list=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=="#":
                i_list.append(i)
                j_list.append(j)
    
    answer = [min(i_list), min(j_list),max(i_list)+1, max(j_list)+1]
    return answer