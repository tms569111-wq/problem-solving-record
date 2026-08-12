# 막대 모양 그래프는 그냥 한 정점에서 다음으로 가고 그걸 끝까지 반복했을 때에
# 본래 위치로 돌아오지 않으면 막대그래프이다
# 도넛모양 그래프는 돌아오면
# 8자 모형 도넛 모형이 같은 정점에서 2개면
#근데 도넛과 8자를 어떻게 구분하지?
# 도넛은 중간에 간선이 2개인 녀석이 있고 도넛은 없다. 이게 중요하군.
# 풀이는 이렇게 할 듯. 먼저 맨 처음 주어진 정점을 찾아야 함 문제에서는 그냥 맨처음 주어진 a가 정점 같기도 한데
# 예제만 그럴 듯? 문제에는 그런 내용이 없네 
# dic[a] = b
# dic[b] = c 이런식으로 해서
# 그뒤 그 정점에서 끝까지 갈 때 원래 값으로 돌아오지 못하면 막대 그래프. 
# 원래 값으로 돌아오면 도넛 그래프
# 돌아가다가 어떤 dic에서 dic[a] = [c, g] 이런 식이 있고 c 선택 할 때랑 g 선택할 때랑 다 계속 가다가 a가 오면
# 얘는 8자 그래프 그러려면...어렵군 일단 구현 해보자

def solution(edges):
    MAX = 1000000
    indegree = [0] * MAX
    outdegree =[0] * MAX
    nodes = set()
    
    for a, b in edges:
        outdegree[a] += 1
        indegree[b] += 1
        nodes.add(a)
        nodes.add(b)
    
    created = 0
    stick = 0
    eight = 0
    
    for node in nodes:
        if indegree[node] == 0 and outdegree[node] >= 2:
            created = node
        elif outdegree[node] == 0:
            stick += 1
        elif indegree[node] >= 2 and outdegree[node] == 2:
            eight += 1
    total = outdegree[created]
    donut = total - stick - eight
    return [created, donut, stick, eight]