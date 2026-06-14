def solution(age):
    # 매핑 기준이 되는 알파벳 문자열
    alphabet = "abcdefghij"
    
    # 숫자를 문자열로 바꾼 뒤, 각 자릿수 숫자를 인덱스로 사용하여 알파벳으로 치환
    return "".join([alphabet[int(i)] for i in str(age)])