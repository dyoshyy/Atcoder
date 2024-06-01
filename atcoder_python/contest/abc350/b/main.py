N, Q = map(int, input().split())
T = list(map(int, input().split()))

Teeth = [1] * N
for T_i in T:
  if Teeth[T_i-1] == 1:
    Teeth[T_i-1] = 0
  else:
    Teeth[T_i-1] = 1
  
print(sum(Teeth))