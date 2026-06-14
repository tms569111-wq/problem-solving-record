import heapq
def solution(book_time):
    def to_min(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    times=[]
    for start,end in book_time:
        start_min=to_min(start)
        end_min=to_min(end)+10
        times.append((start_min,end_min))
    times.sort()
    rooms=[]
    for start, end in times:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)
    return len(rooms)