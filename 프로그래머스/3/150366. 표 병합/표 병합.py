from collections import defaultdict
# update와 print는 할만한데
# merge와 unmerge가 문제
# 해쉬같은 걸로?
# 진짜 병합 할 필요는 없고 병합했다고 가정하고 공유하는 값과 공유하는 위치만 리스트로 담으면 될 듯
# defaultdict로 빨리 풀 수 있을 듯
# 일단 어떤 해쉬에 리스트로 하고 [0, 0]

def solution(commands):
    SIZE = 50
    TOTAL = SIZE * SIZE
    parent = list(range(TOTAL))
    
    
    value = [""] * TOTAL
    
    answer = []
    
    def get_index(r, c):
        return (r - 1) * SIZE + (c - 1)
    
    def find(x):
        
        if parent[x] == x:
            return x
        
        parent[x] = find(parent[x])
        
        return parent[x]
    for command in commands:
        
        parts = command.split()
        
        cmd = parts[0]
        
        if cmd == "UPDATE":
            if len(parts) == 4:
                r = int(parts[1])
                c = int(parts[2])
                new_value = parts[3]
                
                cell = get_index(r, c)
        
                root = find(cell)
                value[root] = new_value
            
            else:
                old_value = parts[1]
                new_value = parts[2]
                
                for i in range(TOTAL):
                    if parent[i] == i and value[i] == old_value:
                        value[i] = new_value
            
        elif cmd == "MERGE":
            r1 = int(parts[1])
            c1 = int(parts[2])
            r2 = int(parts[3])
            c2 = int(parts[4])
            cell1 = get_index(r1, c1)
            cell2 = get_index(r2, c2)
            
            root1 = find(cell1)
            root2 = find(cell2)
            if root1 == root2:
                continue
            if value[root1] != "":
                merged_value = value[root1]
            else:
                merged_value = value[root2]
                
            parent[root2] = root1
            value[root1] = merged_value
            
            value[root1] = merged_value
            value[root2] = ""
        elif cmd == "UNMERGE":
            r = int(parts[1])
            c = int(parts[2])
            
            target = get_index(r, c)
            root = find(target)
            
            saved_value = value[root]
            
            members = []
            
            for i in range(TOTAL):
                if find(i) == root:
                    members.append(i)
                    
            for cell in members:
                parent[cell] = cell
                value[cell] = ""
            
            value[target] = saved_value
        else:
            r = int(parts[1])
            c = int(parts[2])

            cell = get_index(r, c)
            
            root = find(cell)
            
            if value[root] == "":
                answer.append("EMPTY")
            else:
                answer.append(value[root])
    return answer