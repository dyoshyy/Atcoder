from math import gcd

def is_geometric_sequence(N, A):
    if N < 2:
        return "No"
    
    numerator = A[1]
    denominator = A[0]
    
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    
    for i in range(1, N):
        current_numerator = A[i]
        current_denominator = A[i-1]
        
        # 約分
        current_divisor = gcd(current_numerator, current_denominator)
        current_numerator //= current_divisor
        current_denominator //= current_divisor
        
        if current_numerator != numerator or current_denominator != denominator:
            return "No"
    
    return "Yes"

N = int(input())
A = list(map(int, input().split()))

print(is_geometric_sequence(N, A))