N, A, B = map(int, input().split())
D = list(map(int, input().split()))
weekDays = A + B
D = [(d % weekDays) for d in D]
D.sort()
D.append(D[0])

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
# print("D:", D)
for i in range(len(D)-1):
  val = (D[i+1]-D[i]) % weekDays
  # print(i, val)
  if val > B:
    print("Yes")
    exit()
  
print("No")
  