S = input()

count = {}
for s in S:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

max_value = max(count.values())

for i in range(1, max_value+1):
  sum = 0
  for key, value in count.items():
    if value == i:
      sum += 1
  
  if sum == 0 or sum == 2:
    pass
  else:
    print('No')
    exit()

print('Yes')