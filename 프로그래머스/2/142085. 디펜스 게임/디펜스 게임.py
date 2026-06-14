import heapq
def solution(n, k, enemy):
    # 이거는 애매 하군...
    # 먼저 최대한 큰 에너미에다가 무적권을 쓸 수도 있지만...
    # 그러다가는 무적권을 쓴 놈을 만나기도 전에 끝나버리고 만다.
    # 그렇다면 일단 무적권을 쓰지 않고 몇 라운드 까지 가나 보고
    # 거기서 큰 놈들 부터 무적권을 쓰는 방식으로 하면 어떨까??
    # 그러나 k나 enemy의 길이가 심상치 않다...
    # 시간복잡도를 고려해야 해...
    # 역시 가장 좋은 방법은 무적권을 쓸 수 있는 k개 만큼 최대값부터 저장해뒀다가
    # 꽉차서 죽을 때가 되면 무적권을 쓰고 enemy에 다음으로 넘어가다 다시 죽을 때 쯤 최대값에 무적권을 쓰기.
    # 이게 정답 같은데...
    # 최대 힙을 쓰면 가능하긴 해...
    if k>=len(enemy):
        return len(enemy)
    heap=[]
    for i in range(len(enemy)):
        now_hp=n-enemy[i]
        if now_hp>=0:
            n=now_hp
            heapq.heappush(heap,-enemy[i])
        elif now_hp<0 and heap==[] and k>0:
            k=k-1
        elif now_hp<0 and heap!=[] and k>0:
            k=k-1
            max_num=heapq.heappop(heap)*(-1)
            if max_num>enemy[i]:
                now_hp+=max_num
                heapq.heappush(heap,-enemy[i])
            else:
                now_hp+=enemy[i]
                heapq.heappush(heap,-max_num)
            n=now_hp
        elif now_hp<0:
            return i
                
    if n>=0:
        return len(enemy)