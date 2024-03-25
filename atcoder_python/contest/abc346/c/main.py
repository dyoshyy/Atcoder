N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A = set(A)
A = [x for x in A if x <= K]

ans = (1+K)*K//2 - sum(A)
print(ans)
