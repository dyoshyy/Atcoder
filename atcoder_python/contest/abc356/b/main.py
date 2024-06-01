N, M = map(int, input().split())
A = list(map(int, input().split()))
nutrients = [0] * M

for i in range(N):
  X = list(map(int, input().split()))
  for j in range(M):
    nutrients[j] += X[j]
    
for i in range(M):
  if nutrients[i] < A[i]:
    print("No")
    exit()

print("Yes")