import heapq
from bisect import bisect_left

def find_kth_nearest(a, b, k):
    n = len(a)
    left, right = -1, 10**9
    
    while right - left > 1:
        mid = (left + right) // 2
        count = bisect_left(a, b) - bisect_left(a, b - mid) + \
                bisect_left(a, b + mid + 1) - bisect_left(a, b)
        
        if count >= k:
            right = mid
        else:
            left = mid
    
    return right

N, Q = map(int, input().split())
a = sorted(map(int, input().split()))

for _ in range(Q):
    b, k = map(int, input().split())
    result = find_kth_nearest(a, b, k)
    print(result)