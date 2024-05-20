N = int(input())
A = []
I = {}
for i in range(N):
  A.append(list(map(int, input().split())))
  I[A[i][0]] = i

A.sort(key=lambda x: x[0], reverse=True)

min_cost = A[0][1]
kept = [A[0]]
for i in range(1, N):
  if A[i][1] <= min_cost:
    min_cost = A[i][1]
    kept.append(A[i])

output = [I[card[0]] + 1 for card in kept]
output.sort()
print(len(output))
print(*output)