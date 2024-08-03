N, M = map(int, input().split())
A = list(map(int, input().split()))

if M >= sum(A):
    print("infinite")
elif N == 1:
    print(min(M, A[0]))
else:
    A.sort()
    
    def calculate_sum(x):
        return sum(min(x, a) for a in A)
    
    left, right = 0, 10**9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if calculate_sum(mid) <= M:
            left = mid
        else:
            right = mid
    
    print(left)