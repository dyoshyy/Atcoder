def count_overlapping_intervals(N, intervals):
    events = []
    
    # イベントリストを作成
    for l, r in intervals:
        events.append((l, 'start'))
        events.append((r, 'end'))
    
    # イベントをソート
    events.sort(key=lambda x: (x[0], x[1] == 'end'))
    
    active_intervals = 0
    overlap_count = 0
    
    # ソートされたイベントをスイープ
    for event in events:
        if event[1] == 'start':
            overlap_count += active_intervals
            active_intervals += 1
        else:
            active_intervals -= 1
    
    return overlap_count

data = input().split()

N = int(data[0])
intervals = []

for i in range(N):
    l = int(data[2 * i + 1])
    r = int(data[2 * i + 2])
    intervals.append((l, r))

# 結果の出力
print(count_overlapping_intervals(N, intervals))