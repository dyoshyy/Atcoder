H, W = map(int, input().split())
S = [input() for _ in range(H)]

# '#'をすべて含む長方形の左上と右下の座標を返す
def get_rect(S):
    top = None
    bottom = None
    left = len(S[0])
    right = -1
    for i in range(len(S)):
        if '#' in S[i]:
            if top is None:
                top = i
            bottom = i
            left = min(left, S[i].index('#'))
            right = max(right, S[i].rindex('#'))
    return (top, left), (bottom, right)

(top, left), (bottom, right) = get_rect(S)

# 矩形領域内が'#'または'?'のみで構成されているかどうか
for i in range(top, bottom+1):
    for j in range(left, right+1):
        if S[i][j] not in ['#', '?']:
            print('No')
            exit()

# 矩形領域以外が'.'または'?'のみで構成されているかどうか
for i in range(H):
    for j in range(W):
        if i < top or i > bottom or j < left or j > right:
            if S[i][j] not in ['.', '?']:
                print('No')
                exit()

print('Yes')