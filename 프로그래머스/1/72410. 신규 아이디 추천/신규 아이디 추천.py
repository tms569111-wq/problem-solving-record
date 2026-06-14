import re
def solution(new_id):
    answer = ''
    # 1. 소문자 변환
    new_id=new_id.lower()
    # 2 단계 제거
    new_id=re.sub(r'[^a-z0-9\-_.]','',new_id)
    # 3단계 마침표 중복 제거(위에는 노가다인데 이건 걍 모르겠네)

    new_id=re.sub(r'\.+','.',new_id)
    # 4단계 마침표 처음 제거
    new_id = new_id.strip('.')
    # 5단계
    if new_id=="":
        new_id='a'
    # 6단계
    if len(new_id)>=16:
        new_id=new_id[:15]
        if "."==new_id[-1]:
            new_id=new_id[:-1]
    # 7단계.
    while len(new_id)<3:
        new_id=new_id+new_id[-1]
        
    answer = new_id
    return answer