Xa, Ya = map(int, input().split())
Xb, Yb = map(int, input().split())
Xc, Yc = map(int, input().split())

VecAB = (Xb - Xa, Yb - Ya)
VecBC = (Xc - Xb, Yc - Yb)
VecCA = (Xa - Xc, Ya - Yc)

def is_perpendicular(vec1, vec2):
  dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
  return dot_product == 0

if is_perpendicular(VecAB, VecBC) or is_perpendicular(VecBC, VecCA) or is_perpendicular(VecCA, VecAB):
  print("Yes")
else:
  print("No")
