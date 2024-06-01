N = int(input())
S = []
sumRate = 0
for i in range(N):
  s, c = input().split()
  S.append(s)
  sumRate += int(c)

S.sort()
print(S[sumRate%N])

