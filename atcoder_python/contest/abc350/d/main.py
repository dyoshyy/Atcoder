from collections import defaultdict

N, M = map(int, input().split())
if M == 0:
  print(0)
  exit()
friends = defaultdict(set)

for _ in range(M):
    A, B = map(int, input().split())
    friends[A].add(B)
    friends[B].add(A)

ans = 0
for i in range(1, N+1):
    potential_friends = set()
    for friend in friends[i]:
        potential_friends |= friends[friend]
    potential_friends -= friends[i]
    potential_friends.discard(i)
    for friend in potential_friends:
        friends[i].add(friend)
        friends[friend].add(i)
    ans += len(potential_friends)

print(ans)