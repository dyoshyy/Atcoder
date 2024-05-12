N = int(input())
A = []
max_head_height = 0
sum_shoulder_height = 0
for i in range(N):
  A_i, B_i = map(int, input().split())
  max_head_height = max(max_head_height, B_i - A_i)
  sum_shoulder_height += A_i

print(max_head_height + sum_shoulder_height)
  
