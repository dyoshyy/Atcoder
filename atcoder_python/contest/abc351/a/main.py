A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = sum(A[:9])
B_score = sum(B)

print(A_score-B_score+1)