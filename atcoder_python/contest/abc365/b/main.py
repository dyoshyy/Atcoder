N = int(input())
A = list(map(int, input().split()))

max_value = max(A)
second_max_value = max([x for x in A if x != max_value])
second_max_index = A.index(second_max_value)

print(second_max_index + 1)