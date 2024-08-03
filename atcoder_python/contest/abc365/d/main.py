def solve(N, S):
    wins = 0
    prev_hand = None
    
    for aoki_hand in S:
        if aoki_hand == 'R':
            if prev_hand != 'P':
                wins += 1
                prev_hand = 'P'
            elif prev_hand != 'R':
                prev_hand = 'R'
            else:
                break
        elif aoki_hand == 'P':
            if prev_hand != 'S':
                wins += 1
                prev_hand = 'S'
            elif prev_hand != 'P':
                prev_hand = 'P'
            else:
                break
        else:  # aoki_hand == 'S'
            if prev_hand != 'R':
                wins += 1
                prev_hand = 'R'
            elif prev_hand != 'S':
                prev_hand = 'S'
            else:
                break
    
    return wins

N = int(input())
S = input().strip()

print(solve(N, S))