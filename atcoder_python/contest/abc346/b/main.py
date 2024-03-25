W, B = map(int, input().split())
S = "wbwbwwbwbwbw" * ((W+B)//12 + 2)
# print(S)

for i  in range(len(S)-(W+B)+1):
  str = S[i:i+W+B]
  num_w = str.count("w")
  num_b = str.count("b")
  if num_w == W and num_b == B:
    print("Yes")
    exit()
  
print("No")
