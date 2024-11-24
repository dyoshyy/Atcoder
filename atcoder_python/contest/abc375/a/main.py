N = int(input())
S = input()

sum = 0
for i in range(0, N-2):
  if S[i] == "#" and S[i+1] == "." and S[i+2] == "#":
    sum += 1
    
print(sum)