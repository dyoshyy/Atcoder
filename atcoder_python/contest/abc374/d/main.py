# 入力の受け取り
N, S, T = map(int, input().split())

A = []
B = []
C = []
D = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# 2点間の距離を計算する関数
def calc_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# 2点間を速度vで移動するのにかかる時間を計算する関数
def calc_time(x1, y1, x2, y2, v):
    return calc_distance(x1, y1, x2, y2) / v

# 初期化
INF = float('inf')
dp = [[INF] * (2 * N) for _ in range(1 << N)]
start_X, start_Y = 0, 0

edge_points = []
for i in range(N):
    edge_points.append((A[i], B[i]))
    edge_points.append((C[i], D[i]))

# スタート地点から各線分の端点への初期化
for i in range(N):
    for j in range(2):
        x, y = edge_points[i * 2 + j]
        dp[1 << i][i * 2 + j] = calc_time(start_X, start_Y, x, y, S)

# 動的計画法による状態遷移
for mask in range(1 << N):
    for i in range(2 * N):
        if dp[mask][i] == INF:
            continue
        for next_seg in range(N):
            if mask & (1 << next_seg):
                continue
            # 次の線分の端点について遷移を考える
            for j in range(2):
                next_point = 2 * next_seg + j
                x1, y1 = edge_points[i]
                x2, y2 = edge_points[next_point]
                new_mask = mask | (1 << next_seg)

                # 現在の端点から次の端点まで移動する時間（速度Sで計算）
                move_time = calc_time(x1, y1, x2, y2, S)

                # 次の線分を照射しながら移動する時間（速度Tで計算）
                x3, y3 = edge_points[2 * next_seg]
                x4, y4 = edge_points[2 * next_seg + 1]
                print_time = calc_time(x3, y3, x4, y4, T)

                # 線分上の移動と印字の時間を合わせてdpテーブルを更新
                dp[new_mask][next_point] = min(
                    dp[new_mask][next_point],
                    dp[mask][i] + move_time + print_time
                )

# 最小時間を求める
ans = INF
for i in range(2 * N):
    ans = min(ans, dp[(1 << N) - 1][i])

# 結果を出力
print(ans)
