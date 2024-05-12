N, K = map(int, input().split())
P = list(map(int, input().split()))

if K == 1:
  print(0)
  exit()

# 各要素の値とインデックスをペアとして保存
pairs = [(P[i], i) for i in range(N)]

# 値に基づいてソート
pairs.sort()

# スライディングウィンドウ内の最大インデックスと最小インデックスを保存
min_index = max_index = pairs[0][1]

# 最小値を無限大で初期化
min_diff = float('inf')

for i in range(1, K-1):
  # スライディングウィンドウ内の最大インデックスと最小インデックスを更新
  min_index = min(min_index, pairs[i][1])
  max_index = max(max_index, pairs[i][1])

for i in range(K-1, N):
  
  # スライディングウィンドウ内の最大インデックスと最小インデックスを更新
  min_index = min(min_index, pairs[i][1])
  max_index = max(max_index, pairs[i][1])
  
  # 最大インデックスと最小インデックスの差を計算
  diff = max_index - min_index

  # 最小値を更新
  min_diff = min(min_diff, diff)

  # スライディングウィンドウを移動
  if pairs[i - K + 1][1] == min_index:
    min_index = min(pairs[i - K + 2:i + 1], key=lambda x: x[1])[1]
  if pairs[i - K + 1][1] == max_index:
    max_index = max(pairs[i - K + 2:i + 1], key=lambda x: x[1])[1]

print(min_diff)