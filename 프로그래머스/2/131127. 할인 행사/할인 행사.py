from collections import Counter
def solution(want, number, discount):
    #슬라이딩 윈도우 사용하는 문제
    # want를 dict로 만들고 number를 더함
    # dict를 복사하되 다 값이 0인 dict를 만듦
    #discount 10개씩 10일을 슬라이딩 윈도우로 1일씩 더해서 want dict와 0값인 dict가 같으면 1일을 몇일 더했나 구함.
    wish={}
    answer=0
    for i in range(len(want)):
        wish[want[i]]=number[i]
    for j in range(len(discount)-9):
        discount_dict = Counter(discount[j:j+10])
        if wish==discount_dict:
            answer+=1
                        
    
    return answer