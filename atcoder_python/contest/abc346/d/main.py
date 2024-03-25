N = int(input())
S = input()
C = list(map(int, input().split()))
min_cost = float("inf")
for i in range(N):
  # 0から始まるコスト
  cost = 0
  
  for j in range(0, i):
    if j % 2 == 0:
      if S[j] == "1":
        cost += C[j]
      else:
        pass
    else:
      if S[j] == "1":
        pass
      else:
        cost += C[j]
  for j in range(i, N):
    if j % 2 == 0:
      if S[j] == "1":
        pass
      else:
        cost += C[j]
    else:
      if S[j] == "1":
        cost += C[j]
      else:
        pass
  min_cost = min(min_cost, cost)
  
  # 1から始まるコスト
  cost = 0
  for j in range(0, i):
    if j % 2 != 0:
      if S[j] == "1":
        cost += C[j]
      else:
        pass
    else:
      if S[j] == "1":
        pass
      else:
        cost += C[j]
  for j in range(i, N):
    if j % 2 != 0:
      if S[j] == "1":
        pass
      else:
        cost += C[j]
    else:
      if S[j] == "1":
        cost += C[j]
      else:
        pass
  min_cost = min(min_cost, cost)
    
print(min_cost)
