A, B, C, D = map(int, input().split())
space_in_a_row = 0
space = 0

# x軸方向
if A % 2 == 1:
  A_normalized = A + 1
  if A % 4 == 1:
    space_in_a_row += 1.5
  elif A % 4 == 3:
    space_in_a_row += 0.5
else:
  A_normalized = A

if C % 2 == 1:
  C_normalized = C - 1
  if C % 4 == 1:
    space_in_a_row += 1.5
  elif C % 4 == 3:
    space_in_a_row += 0.5
else:
  C_normalized = C
  
if A_normalized <= C_normalized:
  x_boxes = (C_normalized - A_normalized) // 2

if x_boxes % 2 == 0:
  # 偶数個のブロックの場合、面積４×x_boxes/2の面積
  space_in_a_row += 4 * x_boxes // 2
else:
  # 奇数個のブロックの場合、面積４×(x_boxes-1)/2の面積
  space_in_a_row += 4 * (x_boxes - 1) // 2
  if A_normalized % 4 == 0:
    # 面積３のブロックを足す
    space_in_a_row += 3
  elif A_normalized % 4 == 2:
    # 面積１のブロックを足す
    space_in_a_row += 1

# y軸方向
if B % 2 == 1:
  B_normalized = B + 1
else:
  B_normalized = B

if D % 2 == 1:
  D_normalized = D - 1
else:
  D_normalized = D
  
if B_normalized <= D_normalized:
  y_boxes = (D_normalized - B_normalized) // 2

if B % 2 == 1 and D % 2 == 1:
  y_boxes += 1
elif B % 2 == 1 or D % 2 == 1:
  space +=  2 * (C_normalized - A_normalized) // 4

if y_boxes > 0:
  space += space_in_a_row * y_boxes
else:
  space *= space_in_a_row

print(space * 2)
  


