A, B = map(int, input().split())
C = [1, 2, 3]
if A == B:
  print(-1)
else:
  print(*[i for i in C if i != A and i != B])