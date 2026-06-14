def solution(myString, pat):
    if len(pat)>len(myString):
        return 0
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0