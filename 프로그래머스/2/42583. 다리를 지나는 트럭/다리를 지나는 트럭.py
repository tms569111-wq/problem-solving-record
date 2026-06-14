from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    wait = deque(truck_weights)
    current_weight = 0
    while wait or current_weight > 0:
        time += 1
        out = bridge.popleft()
        current_weight -= out
        if wait and current_weight + wait[0] <= weight:
            truck = wait.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

    return time