def solution(spell, dic):
    
    for i in dic:
        check=0
        for j in spell:
            if j in i:
                check+=1
        if len(spell) == check:
            return 1

    return 2