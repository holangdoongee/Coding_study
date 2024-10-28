# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    current_weights = 0
    while len(truck_weights) != 0:
        time += 1
        current_weights -= bridge.popleft()
        
        if current_weights + truck_weights[0] <= weight:
            current_weights += truck_weights[0]
            bridge.append(truck_weights[0])
            truck_weights.popleft()
            # bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    
    print(time)
    time += bridge_length
    
    return time