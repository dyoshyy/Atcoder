N = int(input())

tmp = ""
for i in range(N):
  ryouri = input()
  
  if tmp == "sweet" and ryouri == "sweet" and i < N - 1:
    print("No")
    exit()
    
  tmp = ryouri
  
print("Yes")