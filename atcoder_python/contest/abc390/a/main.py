A = list(map(int, input().split()))

wrong_nums = []
for i in range(5):
    if A[i] != i+1:
        wrong_nums.append(A[i])

if len(wrong_nums) == 2 and abs(wrong_nums[0] - wrong_nums[1]) == 1:
    print("Yes")
else:
    print("No")

    