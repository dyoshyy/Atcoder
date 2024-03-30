N, A, B = map(int, input().split())
D = list(map(int, input().split()))
weekDays = A + B
D = [(d % weekDays) for d in D]
D.sort()

# print(D)
# if max(D) - min(D) > A:
#   print("No")
#   exit()

# for d in range(weekDays):
#   isAcceptable = True
#   for n in range(N):
#     if (d + D[n]) % weekDays <= A and ((d + D[n]) % weekDays != 0):
#       pass
#     else:
#       isAcceptable = False
#       break
#   if isAcceptable:
#     print("Yes")
#     exit()
  
# print("No")

for d in range(weekDays):
  if (0 < (d + D[0]) % weekDays) and ((d + D[0]) % weekDays <= A ) and (0 < (d + D[-1]) % weekDays) and ((d + D[-1]) % weekDays <= A):
      print("Yes")
      exit()
  
print("No")
  