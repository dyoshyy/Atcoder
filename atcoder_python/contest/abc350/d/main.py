def dfs(v, G, visited):
    stack = [v]
    count = 0
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        count += 1
        for next_node in G[node]:
            if not visited[next_node]:
                stack.append(next_node)
    return count

N, M = map(int, input().split())
if M == 0:
  print(0)
  exit()
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

visited = [False] * N
allEdges = 0

for v in range(N):
    if visited[v]:
        continue
    num_connected_nodes = dfs(v, G, visited)
    allEdges += num_connected_nodes * (num_connected_nodes - 1) // 2

print(allEdges - M)