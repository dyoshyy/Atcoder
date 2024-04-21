N = int(input())
A = list(map(int, input().split()))

if A == sorted(A):
  print(0)
  exit()
  
position = [0] * N

for i, A_i in enumerate(A):
    position[A_i-1] = i
swaps = []

for i in range(N):
    if A[i] != A[position[i]]:
        tmp = A[i]
        A[i] = A[position[i]]
        A[position[i]] = tmp
        swaps.append((i+1, position[i]+1))
        position[tmp-1] = position[i]
        position[i] = i


k = len(swaps)
print(k)
for i in range(k):
  print(*swaps[i])