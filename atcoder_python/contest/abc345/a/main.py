
S = input()

if S[0] == "<" and S[-1] == ">":
  if S[1:-1] == "="*len(S[1:-1]):
    print("Yes")
  else:
    print("No")
else:
  print("No")