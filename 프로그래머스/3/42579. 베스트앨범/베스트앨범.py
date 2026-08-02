from collections import defaultdict
def solution(genres, plays):
    genres_dic = defaultdict(int)
    genres_plays_dic = defaultdict(lambda : [[-1, -1], [-1, -1]])
    n = len(genres)
    
    for i in range(n): 
        genres_dic[genres[i]] += plays[i]
        max_check = genres_plays_dic[genres[i]]
        
        if max_check[0][0] < plays[i]:
            genres_plays_dic[genres[i]][1][0] = genres_plays_dic[genres[i]][0][0]
            genres_plays_dic[genres[i]][1][1] = genres_plays_dic[genres[i]][0][1]
            
            genres_plays_dic[genres[i]][0][0] = plays[i]
            genres_plays_dic[genres[i]][0][1] = i
        
        elif max_check[1][0] < plays[i]:
            genres_plays_dic[genres[i]][1][0] = plays[i]
            genres_plays_dic[genres[i]][1][1] = i
    
    genres_sum = []
    
    for key, value in genres_dic.items():
        genres_sum.append([key, value])
        
    genres_sum.sort(key = lambda x : (-x[1]))
    
    answer = []
    
    for sorted_genres in genres_sum:
        if genres_plays_dic[sorted_genres[0]][0][0] == -1:
            continue
        else:
            answer.append(genres_plays_dic[sorted_genres[0]][0][1])
        
        if genres_plays_dic[sorted_genres[0]][1][0] == -1:
            continue
        else:
            answer.append(genres_plays_dic[sorted_genres[0]][1][1])
        
    return answer