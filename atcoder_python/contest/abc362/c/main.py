N = int(input())
ranges = [list(map(int, input().split())) for _ in range(N)]

L = [x[0] for x in ranges]
R = [x[1] for x in ranges]

sum_L = sum(L)
sum_R = sum(R)

if sum_L > 0 or sum_R < 0:
  print("No")
  exit()
  
X = L
sum = sum_L

for i in range(N):
  if sum == 0:
    print("Yes")
    print(*X)
    exit()
  if sum + (R[i] - X[i]) < 0:
      sum += (R[i] - X[i])
      X[i] = R[i]
  elif sum < 0 and sum + (R[i] - X[i]) >= 0:
      X[i] += -sum
      sum = 0

if sum == 0:
  print("Yes")
  print(*X)
else:
    
  print("No")


  