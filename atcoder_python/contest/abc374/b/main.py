S = input()
T = input()

if S == T:
  print("0")
else:
  i = 0
  while i < min(len(S), len(T)):
    if S[i] != T[i]:
      print(i + 1)
      break
    i += 1
  else:
    print(i + 1)