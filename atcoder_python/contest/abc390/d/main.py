from collections import deque

def calculate_xor_values(bags):
    reachable = set()
    visited = set()
    stack = deque()
    
    initial_state = tuple(sorted(bags))
    stack.append(initial_state)
    visited.add(initial_state)
    
    while stack:
        state = stack.pop()
        xor_value = 0
        for count in state:
            xor_value ^= count
        reachable.add(xor_value)
        
        for i in range(len(state)):
            if state[i] > 0:
                for j in range(len(state)):
                    if i != j:
                        new_state = list(state)
                        new_state[j] += new_state[i]
                        new_state[i] = 0
                        new_state_tuple = tuple(sorted(new_state))
                        if new_state_tuple not in visited:
                            visited.add(new_state_tuple)
                            stack.append(new_state_tuple)
    
    return len(reachable)

N = int(input())
bags = list(map(int, input().split()))

result = calculate_xor_values(bags)
print(result)