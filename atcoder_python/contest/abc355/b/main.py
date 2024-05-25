N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C.sort()

for i in range(1, N + M):
    if C[i] in A and C[i-1] in A:
        print("Yes")
        exit()

print("No")
  