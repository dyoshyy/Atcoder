N = int(input())
K = list(map(int, input().split()))

sum = sum(K)
min_max = float('inf')

for mask in range(1 << N):
  A_sum = 0
  for i in range(N):
    if mask & (1 << i):
      A_sum += K[i]
      
  B_sum = sum - A_sum
  min_max = min(min_max, max(A_sum, B_sum))
  
print(min_max)
