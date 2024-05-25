N, T = map(int, input().split())
A = list(map(int, input().split()))

# 初期化
row_count = [0] * N
col_count = [0] * N
diag1_count = 0
diag2_count = 0

# マス目のインデックス計算
cell_to_position = {}
for i in range(N):
    for j in range(N):
        cell_to_position[N * i + j + 1] = (i, j)

# ターンごとの処理
for turn in range(T):
    value = A[turn]
    if value in cell_to_position:
        i, j = cell_to_position[value]
        row_count[i] += 1
        col_count[j] += 1
        if i == j:
            diag1_count += 1
        if i + j == N - 1:
            diag2_count += 1
        
        # ビンゴのチェック
        if row_count[i] == N or col_count[j] == N or diag1_count == N or diag2_count == N:
            print(turn + 1)
            exit()
print(-1)