N = int(input())
A = list(map(int, input().split()))

balls = []
for i in range(N):
  # ball_size = pow(2, A[i])
  ball_size = A[i]
  balls.append(ball_size)
  if len(balls) <= 1:
    continue
  elif balls[-1] != balls[-2]:
    continue
  else:
    while len(balls) > 1:
      if balls[-1] == balls[-2]:
        balls.pop()
        balls[-1] = balls[-1] + 1
      else:
        break

print(len(balls))