dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    stack = [(x, y)]
    count = 0
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = True
            count += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                elif S[nx][ny] == '.' and not visited[nx][ny]:
                    stack.append((nx, ny))
                elif S[nx][ny] == '0' and not zero_visited[nx][ny]:
                    zero_visited[nx][ny] = True
                    count += 1
    return count

H, W = map(int, input().split())
S = [input() for _ in range(H)]
visited = [[False]*W for _ in range(H)]
zero_visited = [[False]*W for _ in range(H)]
max_size = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            if i != 0:
                S[i-1] = S[i-1][:j] + '0' + S[i-1][j+1:]
            if i != H-1:
                S[i+1] = S[i+1][:j] + '0' + S[i+1][j+1:]
            if j != 0 and j != W-1:
                S[i] = S[i][:(j-1)] + '0#0' + S[i][j+2:]
            elif j == 0:
                S[i] = '#0' + S[i][2:]
            elif j == W-1:
                S[i] = S[i][:j-1] + '0#'

for i in range(H):
    for j in range(W):
        if S[i][j] == '.' and not visited[i][j]:
            zero_visited = [[False]*W for _ in range(H)]
            ans = dfs(i, j)
            max_size = max(max_size, ans)

if max_size == 0:
    max_size = 1
print(max_size)