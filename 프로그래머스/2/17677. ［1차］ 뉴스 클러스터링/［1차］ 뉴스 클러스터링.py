from collections import Counter
def solution(str1, str2):
    #일단 합집합이랑 여집합 만들기 전에 자르기 부터 해야 한다. 일단 lower로 소문자부터 만들고 숫자, 특수문자, 공백을 없애는 전처리를 한다.
    arr1=[]
    arr2=[]
    for i in range(len(str1)-1):
        pair = str1[i:i+2].lower()
        if pair.isalpha():
            arr1.append(pair)
    for j in range(len(str2)-1):
        pair = str2[j:j+2].lower()
        if pair.isalpha():
            arr2.append(pair)
    set_str1=Counter(arr1)
    set_str2=Counter(arr2)
    a=sum((set_str1|set_str2).values())
    b=sum((set_str1&set_str2).values())
    if a==0:
        return 65536
    z=int(((b/a)*65536))
    answer = z
    return answer