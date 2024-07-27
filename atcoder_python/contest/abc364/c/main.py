N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
B = list(map(int, input().split()))
B.sort(reverse=True)

sum_A = 0
sum_B = 0

for i in range(N):
  sum_A += A[i]
  sum_B += B[i]
  if sum_A > X or sum_B > Y:
    print(i+1)
    exit()

print(N)

