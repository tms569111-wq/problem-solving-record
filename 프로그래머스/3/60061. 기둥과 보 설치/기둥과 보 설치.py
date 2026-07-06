def solution(n, build_frame):
    # 보와 기둥이라...
    # 기둥은 세로로 2칸 즉 [x, y, a, b]에서 a는 0이면 x, y랑 x, y+1이 기둥이 세워지고
    # 보는 가로로 두 칸인데, x, y랑 ,x + 1,y에서 기둥이 세워지게 됨
    # 기둥은 바닥에 있어야 되거나, 보의 한쪽 끝 위, 다른 기둥위
    # 즉 y == 0 or x, y에 보가 있거나, x, y에 기둥이 있으면 됨
    # 겹치는 거 고려
    # 아 제한사항에 겹치는 거 없네
    # 삭제 시에는 상하좌우를 살펴봐야 함.
    # 기둥이 없어졌을 때에는 
    # x, y랑 x, y + 1이 없어지니까
    # x, y에  보가 있으면? 어차피 기둥은 상관 없음 기둥이 누르고 있는 것 뿐이니까
    # x, y+1는 상관 있음 그 보가 다른 보와 연결되거나, 왼쪽 부분이 없어졌으니 오른쪽이 기둥에 있어야 함
    # 보가 없어지면...
    # x, y랑 x + 1, y가 없어지니까
    # 다른 보가 붙어 있으면 그 보가 다른 쪽 기둥 위에 있거나 다른 쪽 연결 되어 있어야 함
    # 위에 기둥이 있으면 기둥이 있는 곳에 밑에 기둥이 있거나 다른 보가 있어야 함
    # 와 까다롭네
    # 대신 시간 복잡도는 완전 널널하네 완전탐색해도 될 듯
    # 어우 ;; 복잡하네 그냥 1만 씩 1000번이니까 
    # 얘가 규칙 만족하는지 각 점마다 체크나 할 걸 개 빡세다
    structures = set()
    def is_vaild(x, y, a):
        if a == 0:
            return (
                y == 0 or 
                (x, y - 1, 0) in structures or
                (x - 1, y, 1,) in structures or
                (x, y, 1) in structures
           )
        else:
            return (
                (x, y -1, 0) in structures or
                (x + 1, y - 1, 0) in structures or
                ((x - 1, y, 1) in structures and (x + 1, y, 1) in structures) 
           )
    def is_vaild_all():
        for x, y, a in structures:
            if not is_vaild(x, y, a):
                return False
        return True
    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 1:
            structures.add(item)
            if not is_vaild_all():
                structures.remove(item)
        else:
            structures.remove(item)
            if not is_vaild_all():
                structures.add(item)
                
    return sorted([list(s) for s in structures], key = lambda x: (x[0], x[1], x[2]))