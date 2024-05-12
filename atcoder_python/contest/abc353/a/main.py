N = int(input())
H = list(map(int, input().split()))

for i, h in enumerate(H[1:]):
  if h > H[0]:
    print(i+2)
    exit()

print("-1")
