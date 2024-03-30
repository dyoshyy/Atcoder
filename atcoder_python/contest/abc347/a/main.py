N, K = input().split()
K = int(K)
A = list(map(int, input().split()))

# print(N, K, A)
ans = []

for a in A:
  if a % K == 0:
    ans.append(int(a/K))
  
ans.sort()
print(*ans)
