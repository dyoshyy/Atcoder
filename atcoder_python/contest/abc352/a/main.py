N, X, Y, Z = map(int, input().split())

if X < Y:
  if X <= Z and Z <= Y:
    print("Yes")
    exit()
else:
  if Y <= Z and Z <= X:
    print("Yes")
    exit()
    
print("No")

