H, W = map(int, input().split())
S_i, S_j = map(int, input().split())

grid = [list(input()) for _ in range(H)]
X = input()

for x in X:
  if x == "L":
    if S_j >= 2 and grid[S_i-1][S_j - 2] == ".":
      S_j -= 1
  elif x == "R":
    if S_j <= W-1 and grid[S_i-1][S_j] == ".":
      S_j += 1
  elif x == "U":
    if S_i >= 2 and grid[S_i-2][S_j-1] == ".":
      S_i -= 1
  elif x == "D":
    if S_i <= H-1 and grid[S_i][S_j - 1] == ".":
      S_i += 1
      
print(S_i, S_j)