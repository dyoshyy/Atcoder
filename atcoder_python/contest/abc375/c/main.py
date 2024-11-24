N = int(input())
Grid = [list(input()) for _ in range(N)]

for i in range(N//2):
  print("i: ", i)
  tmp_Grid = [row[:] for row in Grid]
  for j in range(i, N-i):
    # print("i: ", i, "j: ", j, "N-j-1: ", N-j-1)
    # print("".join([row[N-1-j] for row in tmp_Grid[i:N-i]]))
    Grid[j][i:N-i] = [row[N-j-1] for row in tmp_Grid[i:N-i]]
  
  print("".join(Grid))

for i in range(N):
  print("".join(Grid[i]))
      