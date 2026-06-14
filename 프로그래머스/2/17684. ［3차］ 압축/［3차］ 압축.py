import string
def solution(msg):
    dic={letter:i+1 for i, letter in enumerate(string.ascii_uppercase)}
    z=len(msg)
    a=0
    answer = []
    q=26
    while a<z:
        b=msg[a]
        while b in dic:
            a+=1
            if a>=z:
                break
            b+=msg[a]
        if b in dic:
            answer.append(dic[b])
        else:
            c=b[:-1]
            answer.append(dic[c])
            q=q+1
            dic[b]=q
            a-=1
        a+=1
    return answer
        
        
            
                
            
            
        
    # 일단 처음에는 무조건 1단어니까 2단어 해도 사전추가 27
    # 여러 단어가 있을 때? 내생각에는 for문의 for로 2중포문해서 일단 현재입력 기준으로 for문 한 개 다음 글자를 추가해가고
    # 다음 글자가 있으면 계속 추가, 없으면 바뀐 걸 i로...근데 이러면 while이 나은 것 같기도 함.
    # 일단 dic해쉬
    