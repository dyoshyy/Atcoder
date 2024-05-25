import sys

def interactive_sum(N, L, R):
    def query(l, r):
        print(f"? {l} {r}")
        sys.stdout.flush()
        response = int(input().strip())
        return response

    def sum_range(L, R):
        if L > R:
            return 0
        if L == R:
            return query(L, L) % 100
        mid = (L + R) // 2
        left_sum = sum_range(L, mid)
        right_sum = sum_range(mid + 1, R)
        return (left_sum + right_sum) % 100

    total_sum = sum_range(L, R)
    print(f"! {total_sum}")
    exit()

# 入力の読み込み
N, L, R = input().split()

interactive_sum(N, L, R)
