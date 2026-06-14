from itertools import product 
def solution(word):
    words=[]
    vowels=['A','E','I','O','U']
    
    def dfs(current_word):
        if len(current_word)>5:
            return
        if current_word:
            words.append(current_word)
            
        for v in vowels:
            dfs(current_word+v)
    dfs("")
        
    words.sort()
    return words.index(word)+1