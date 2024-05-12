N = int(input())
A = list(map(int, input().split()))
A.sort()

M = 10**8

count_over_M = 0
cnt = [0] * (M+1)

# 10**8を超えるペアが何個あるかを数える
for a in A:
  cnt[a] += 1
for i in range(M):
  cnt[i+1] += cnt[i]

for a in A:
  count_over_M += N - cnt[M-a-1]
  if 2 * a >= M:
    count_over_M -= 1
  
count_over_M //= 2
  
sum_A = sum(A)
sum = sum_A * (N-1)
sum -= count_over_M * M
print(sum)
