L, R = map(int, input().split())
ans = []

while L != R:
    i = 0
    while L % pow(2, i+ 1) == 0 and L + pow(2, i + 1) <= R:
        i += 1
    ans.append((L, L + pow(2, i) ))
    L += pow(2, i) 

print(len(ans))
for a in ans:
    print(a[0], a[1])