S = input()
T = input()

if T[-1] == 'X':
  T = T[:2]

i = 0
for t in T:
  found = False
  while i < len(S):
    # print(i, S[i].upper(), t)
    if S[i].upper() == t:
      i += 1
      found = True
      break
    else:
      i += 1
  if not found and i == len(S):
      print('No')
      exit()

print('Yes')