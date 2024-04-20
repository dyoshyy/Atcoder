import heapq

def heap_sort(arr):
    n = len(arr)
    swaps = []

    heapq.heapify(arr)
    end = n-1
    while end > 0:
        arr[0], arr[end] = arr[end], arr[0]
        swaps.append((0+1, end+1))
        end -= 1
        sift_down(arr, 0, end)

    return arr, swaps

def sift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if arr[swap] < arr[child]:
            swap = child
        if child + 1 <= end and arr[swap] < arr[child + 1]:
            swap = child + 1
        if swap != root:
            arr[root], arr[swap] = arr[swap], arr[root]
            root = swap
        else:
            return

N = int(input())
A = list(map(int, input().split()))

if A == sorted(A):
  print(0)
  exit()

A, swaps = heap_sort(A)

k = len(swaps)
print(k)
for i in range(k):
  print(*swaps[i])