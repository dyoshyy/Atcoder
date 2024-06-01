N, K = map(int, input().split())
A = list(map(int, input().split()))

start_count = 0
remaining_seats = K

for a in A:
  if a <= remaining_seats:
    remaining_seats -= a
    continue
  else:
    start_count += 1
    remaining_seats = K
    remaining_seats -= a

print(start_count+1)
