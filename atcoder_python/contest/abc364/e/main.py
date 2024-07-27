# 入力を受け取る
N, X, Y = map(int, input().split())
dishes = [list(map(int, input().split())) for _ in range(N)]

# 料理を甘さとしょっぱさの合計値でソート
dishes.sort(key=lambda x: x[0] + x[1])

# 最大の料理数を求める
max_dishes = 0
sweet_sum = 0
salty_sum = 0

for sweet, salty in dishes:
    max_dishes += 1
    if sweet_sum + sweet > X or salty_sum + salty > Y:
        break
    sweet_sum += sweet
    salty_sum += salty

# 結果を出力
print(max_dishes)