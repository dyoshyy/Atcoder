H = int(input())

height = 0
days = 0

while H > height:
  days += 1
  height += 2**days
  
print(days+1)