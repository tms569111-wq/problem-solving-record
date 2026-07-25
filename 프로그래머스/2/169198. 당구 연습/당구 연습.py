def solution(m, n, startX, startY, balls):
    answer = []
    def squared_distance(x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2
    
    for x, y in balls:
        candidates = []
        
        if not (startY == y and x < startX):
            candidates.append(
                squared_distance(startX, startY, -x, y)
            )
        if not (startY == y and x > startX):
            candidates.append(
                squared_distance(startX, startY, 2 * m - x, y)
            )
        if not (startX == x and y < startY):
            candidates.append(
                squared_distance(startX, startY, x, -y)
            )
        if not (startX == x and y > startY):
            candidates.append(
                squared_distance(startX, startY, x, 2 * n - y)
            )
        answer.append(min(candidates))
            
    return answer