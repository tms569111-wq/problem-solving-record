def solution(myString, pat):
    check=''
    check_1=0
    for i in range(len(myString)+1):
        if check=='' and pat in myString[0:i]:
            check_1=i
            check=check+myString[0:i]
        elif check!='' and pat in myString[check_1:i]:
            check=check+myString[check_1:i]
            check_1=i
        
    return check