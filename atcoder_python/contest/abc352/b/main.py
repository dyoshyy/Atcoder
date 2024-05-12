S = input()
T = input()
count = 0
ans = []
for i, char in enumerate(T):
  if char == S[count]:
    ans.append(i+1)
    count += 1
    
print(*ans)