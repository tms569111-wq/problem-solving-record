def solution(phone_book):
    hash_map={i: True for i in phone_book}
    for j in phone_book:
        temp=j
        if temp in hash_map and temp!=j:
            return False
    return True