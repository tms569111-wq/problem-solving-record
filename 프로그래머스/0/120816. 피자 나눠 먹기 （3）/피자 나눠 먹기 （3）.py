def solution(slice, n):
    if slice>=n:
        return 1
    else:
        if n%slice!=0:
            return n//slice+1
        else:
            return n//slice